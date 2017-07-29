import logging
import os
from datetime import datetime


def _make_log():
    log_level = logging.DEBUG
    log = logging.getLogger("lgtm")
    log.setLevel(log_level)

    fm = logging.Formatter(
        """[%(levelname)s|%(filename)s:%(lineno)s] """
        """%(asctime)s > %(message)s"""
    )

    sh = logging.StreamHandler()
    sh.setLevel(log_level)
    sh.setFormatter(fm)
    log.addHandler(sh)

    if log_level == logging.DEBUG:
        if not os.path.exists("log/"):
            os.makedirs("log/")
        fh = logging.FileHandler(
            "log/lgtm-{}.log".format(
                datetime.now().strftime("%y-%m-%d-%H-%M-%S")
            ),
            encoding='utf-8'
        )
        fh.setLevel(log_level)
        fh.setFormatter(fm)
        log.addHandler(fh)

    return log


log = _make_log()

