#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-07-18 21:55:10

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from multiprocessing import Pool
import requests
import shutil
import logging
import click
import re
import os


class image_download(object):

    def __init__(self, directory="~/Picture/image_downloader", max_process=4):
        self.directory = os.path.expanduser(directory)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.max_process = max_process

    def get_images(self, urls: dict)->None:
        try:
            with Pool(self.max_process)as pool:
                pool.map(self.get_image, urls.items())
        except:
            logging.error("get images error.")

    def get_image(self, entry: tuple)->None:
        try:
            img_name, href = entry
            res = requests.get(href, stream=True)
            with open(os.path.join(self.directory, img_name), 'wb')as file:
                shutil.copyfileobj(res.raw, file)
                print(img_name + ' success')
        except:
            logging.error("get {} error.".format(href))

    def get_images_links(self, url: str)->dict:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf-8')

        # set the verify false and can detour the web inspect
        soup = BeautifulSoup(webpage, "lxml")
        images = {}
        for link in soup.findAll('a', href=True, rel='nofollow'):
            href = link['href']
            if re.search("jpg|png|gif", href):
                img_name = href.split('/')[-1]
                images[img_name] = href
        return images

    def download(self, article):
        images = self.get_images_links(article)
        self.get_images(images)
        logging.info("download images done.")


@click.command()
@click.option('--directory', default='', help="Directory where to save images.")
@click.argument('web')
def main(directory, web):

    downloader = image_download()
    if directory is not '':
        downloader.directory = directory
    downloader.download(web)
