#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import codecs
import json
import logging
import re
import time

import bs4
import requests

import ikyu
import dl

logger = logging.getLogger(__name__)

from urlparse import urlparse, urlunparse


def run():
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG)

    url_list = []
    with open(args.url_list) as fin:
        for line in fin:
            if line.strip().startswith("#"):
                continue
            url_list.append(line.strip())
    area_urls = []
    for end_url in url_list:
        base_url, num = ikyu.parse_end_url(end_url)
        area_urls.append(base_url)
        for i in range(2, num+1):
            u = ikyu.gen_pagenate_url(base_url, i)
            area_urls.append(u)
    logger.info(json.dumps(area_urls, indent=4))

    for _url in area_urls:
        r = requests.get(_url)
        ikyu.save_html(r)
        review_links = ikyu.extract_links(r.text, 'iconfontStarWrapper')
        logger.info("{} urls found".format(len(review_links)))
        for link in review_links:
            time.sleep(7)
            r = requests.get(link)
            ikyu.save_html(r)
            last_page = ikyu.get_last_page(r.text)
            if last_page is not None:
                print(last_page)
            else:
                print(link)
    return


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('url_list')
    return parser.parse_args()


if __name__ == '__main__':
    run()
