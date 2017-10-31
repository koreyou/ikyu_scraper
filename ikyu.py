#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import json
import logging
import re

import bs4
from urlparse import urlparse, urlunparse, ParseResult


logger = logging.getLogger(__name__)


def parse_end_url(url):
    o = urlparse(url)
    mobj = re.search(ur"/p(?P<page>\d+)/", o.path)
    base_url = url
    num = 1
    if mobj is not None:
        o_path = "/".join(o.path.rstrip("/").split("/")[:-1])
        no = ParseResult(o.scheme, o.netloc, o_path,
                         o.params, o.query, o.fragment)
        base_url = urlunparse(no)
        if not base_url.endswith("/"):
            base_url += "/"
        num = int(mobj.group("page"))
    return base_url, num


def gen_pagenate_url(base_url, page_num):
    if page_num < 2:
        return base_url
    return base_url + "p{}/".format(page_num)


def url_to_filename(url):
    o = urlparse(url)
    return "-".join(o.path.strip("/").split("/")) + ".html"


def save_html(response):
    f = url_to_filename(response.url)
    with codecs.open("urllog/" + f, 'w', 'utf-8') as fout:
        fout.write(response.text)


def get_last_page(html_text):
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    target = None
    for paging in soup.find_all('div', class_="guide_paging"):
        for link in paging.find_all('a'):
            if link.text == u"最後":
                target = link.get("href")
                logger.debug(target)
    return target


def extract_links(html_text, div_region):
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    alist = []
    for review_div in soup.find_all('div', class_=div_region):
        for review_link in review_div.find_all('a'):
            logger.debug(review_link.get("href"))
            alist.append(review_link.get("href"))
    # Remove duplicates
    return list(set(alist))


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
