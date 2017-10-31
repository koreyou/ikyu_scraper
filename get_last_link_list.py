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

logger = logging.getLogger(__name__)


def run():
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG)

    r = requests.get(args.url)
    ikyu.save_html(r)
    review_links = ikyu.extract_links(r.text, "chi_name")
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


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('url')
    return parser.parse_args()


if __name__ == '__main__':
    run()
