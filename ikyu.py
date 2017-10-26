#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import json
import logging
import re

import bs4

logger = logging.getLogger(__name__)


def get_last_page(html_text):
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    target = None
    for paging in soup.find_all('div', class_="guide_paging"):
        for link in paging.find_all('a'):
            if link.text == u"最後":
                target = link.get("href")
                logger.debug(target)
    return target


def extract_links(html_text):
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    alist = []
    for review_div in soup.find_all('div', class_="iconfontStarWrapper"):
        for review_link in review_div.find_all('a'):
            logger.debug(review_link.get("href"))
            alist.append(review_link.get("href"))
    return alist


def run():
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG)

    with codecs.open(args.input_path, 'r', 'utf-8') as fin:
        text = fin.read()

    soup = bs4.BeautifulSoup(text, 'html.parser')
    
    for paging in soup.find_all('div', class_="guide_paging"):
        for link in paging.find_all('a'):
            if link.text == u"最後":
                logger.debug(link.get("href"))


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_path')
    return parser.parse_args()


if __name__ == '__main__':
    run()
