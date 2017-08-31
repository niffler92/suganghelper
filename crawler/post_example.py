import requests



"""
Note that payload is where we fill in check(which subject) and inputText(image)
"""
subject_idx = None
text = None
url = "http://sugang.snu.ac.kr/sugang/ca/ca210.action"
payload = "check={}&inputText={}&ltNo=001&ltNo=002&ltNo=001&ltNo=002&ltNo="\
          "001&ltNo=001&ltNo=001&ltNo=001&ltNo=001&openDetaShtmFg=U000300001"\
          "&openDetaShtmFg=U000300001&openDetaShtmFg=U000300001&openDetaShtmFg="\
          "U000300001&openDetaShtmFg=U000300001&openDetaShtmFg="\
          "U000300001&openDetaShtmFg=U000300001&openDetaShtmFg=U000300001&"\
          "openDetaShtmFg=U000300001&openSchyy=2017&openSchyy=2017&"\
          "openSchyy=2017&openSchyy=2017&openSchyy=2017&openSchyy=2017&"\
          "openSchyy=2017&openSchyy=2017&openSchyy=2017&openShtmFg="\
          "U000200002&openShtmFg=U000200002&openShtmFg=U000200002&"\
          "openShtmFg=U000200002&openShtmFg=U000200002&openShtmFg="\
          "U000200002&openShtmFg=U000200002&openShtmFg=U000200002&"\
          "openShtmFg=U000200002&sbjtCd=051.005&sbjtCd=051.005&sbjtCd="\
          "051.017&sbjtCd=051.017&sbjtCd=326.725A&sbjtCd=3341.362&sbjtCd="\
          "3341.753&sbjtCd=722.212&sbjtCd=M1522.000600&sortKey=&sortOrder="\
          "&workType=I".format(subject_idx, text)
headers = {
    'origin': "http://sugang.snu.ac.kr",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://sugang.snu.ac.kr/sugang/cc/cc210.action",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "_ga=GA1.3.1894202420.1488421061; WMONID=sIRSjVZC3kx; __utma=134997939.1894202420.1488421061.1501193290.1501193290.1; __utmz=134997939.1501193290.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); enter=Y; JSESSIONID=JnQgIuaaNNIRGCjUXmnvgFBel2qZmLQtE4Semyb0SxmRukHs96VJDUXaFaGRLFmN.giants1_servlet_engine1; _ga=GA1.3.1894202420.1488421061; WMONID=sIRSjVZC3kx; __utma=134997939.1894202420.1488421061.1501193290.1501193290.1; __utmz=134997939.1501193290.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); enter=Y; JSESSIONID=TcYSpPwzFTRNQTJHSAq71XtzdHBvR3yuEOiEvFlswZ111OHN9JgRZdVUl2Zaaeav.giants1_servlet_engine1",
    'cache-control': "no-cache",
    'postman-token': "69e36d00-3d56-370d-53c7-86375b824909"
    }

#response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)
