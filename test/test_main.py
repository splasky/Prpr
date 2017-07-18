#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-07-18 21:03:34

from src.image_download import image_download
import os


def test_main():
    article = "https://www.ptt.cc/bbs/KanColle/M.1500338012.A.8C0.html"
    directory = "/tmp/image_download/test/"
    downloader = image_download(directory=directory)
    downloader.download(article)
    assert len([name for name in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, name))]) > 0
