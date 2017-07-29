import datetime, time
import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
import pytesseract
from PIL import Image, ImageGrab, ImageFilter, ImageEnhance
import keyboard
import cv2

from settings import HAKBUN, PASSWORD, classes, coordinates
from utils import log


path = os.path.abspath('./')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def log_in(driver, Id=HAKBUN, password=PASSWORD):
    driver.get('http://sugang.snu.ac.kr')
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

    driver.implicitly_wait(5)
    driver.find_element_by_id('j_username').send_keys(Id)
    driver.implicitly_wait(1)
    driver.find_element_by_id('t_password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="CO010"]/div/div/p[3]/a').click()


def check_classes(driver, classes, save_capture=False):
    assert type(classes) == list, "Must be a list of classes for sugang."

    driver.get('https://sugang.snu.ac.kr/sugang/cc/cc210.action')
    html = driver.page_source
    df_sugang = pd.read_html(html)[0]
    df_sugang = df_sugang[~df_sugang.loc[:,
                          df_sugang.columns == '정원(재학생)']
                          .isnull().values].reindex()

    for idx, values in df_sugang.iterrows():
        full = int(values['정원(재학생)'].split()[0])
        current = values['수강신청인원']

        if full > current and values['교과목명(부제명)'] in classes:
            log.info("Trying to enroll in class {}: ({}/{})".format(
                values['교과목명(부제명)'], int(current), full))
            enrolled = enroll_in_class(driver, values['교과목명(부제명)'],
                                       idx + 1, save_capture)
            if (idx + 1) < len(classes):
                driver.get('https://sugang.snu.ac.kr/sugang/cc/cc210.action')
            time.sleep(0.3)
            #             if enrolled:
            #                 classes.remove(values['교과목명(부제명)'])


def enroll_in_class(driver, classname, index, save_capture=False):
    content = driver.find_element_by_id('content')
    table = content.find_element_by_tag_name('table')
    check = table.find_element_by_xpath('//tr[{}]/td[1]/input[1]'.format(index))
    check.click()

    im = ImageGrab.grab(bbox=(coordinates['x1'], coordinates['y1'],
                              coordinates['x2'], coordinates['y2']))
    save_path = os.path.join(path, 'screenshot/',
                             datetime.datetime.now().strftime('%m%d_%H%M%S.png'))
    im.save(save_path, dpi=(500, 500))

    text = image_to_text(filepath=save_path, save=save_capture)
    log.info("Detected digits for {} : {}".format(save_path, text))

    driver.find_element_by_xpath('//*[@id="inputTextView"]').send_keys(text)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')  # Pop-up

    return True  # FIXME


def image_to_text(img=None, filepath=None, save=False):
    """
    Input can be either image or filepath of the image
    """
    if filepath and img is None:
        img = cv2.imread(filepath, 0)

    img_th = cv2.adaptiveThreshold(img, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    img_th = Image.fromarray(img_th)
    #     w,h = img.shape
    #     img_th = img_th.resize((3*h, 3*w))
    img_th = img_th.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img_th)
    img_th = enhancer.enhance(2)

    text = pytesseract.image_to_string(
        img_th,
        config='--psm 11 --oem 2 -c tessedit_char_whitelist=0123456789')
    text = ''.join(text.split())

    img_th.save(filepath, dpi=(500, 500)) if save else os.remove(filepath)

    return text


def save_remaining(classes):
    pass


def main():
    driver = webdriver.Firefox(executable_path=os.path.join(path, 'geckodriver.exe'))
    log_in(driver, Id=HAKBUN, password=PASSWORD)
    st = time.time()
    while True:
        check_classes(driver, classes, save_capture=True)
        time.sleep(0.3)
        if time.time() - st > 60:
            #  save_remaining(classes)
            break

if __name__ == '__main__':
    main()