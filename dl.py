#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import os
import time

import requests

# https://www.ikyu.com/00000070/review/p27/

# tmpl_url = "https://www.ikyu.com/%08d/review/"
out_html = "%08d.html"
out_suc_html = "%08d-%d.html"

def parse_last_url(url):
    pass


def download_suc_page(base_url, num, out_dir):
    bid = extract_ids(base_url)
    url = "{}p{}/".format(base_url, num)
    filepath = os.path.join(out_dir, out_suc_html % (bid, num))
    r = requests.get(url)
    with codecs.open(filepath, 'w', 'utf-8') as fout:
        print >> fout, r.text


def download_top_page(base_url, out_dir):
    bid = extract_ids(base_url)
    filepath = os.path.join(out_dir, out_html % (bid))
    r = requests.get(base_url)
    with codecs.open(filepath, 'w', 'utf-8') as fout:
        print >> fout, r.text


def extract_ids(base_url):
    elems = base_url.split(".com/")
    try:
        _id = int(elems[1].split("/")[0])
        return _id
    except ValueError:
        _id = int(elems[1].split("/")[1])
        return _id


def download_pages(last_url, dirname):
    elems = last_url.rsplit('/p', 1)
    if len(elems) == 1:
        # no param        
        base_url = elems[0]
        download_top_page(base_url, dirname)
        time.sleep(7)
    else:
        base_url = elems[0] + "/"
        download_top_page(base_url, dirname)
        max_index = elems[1][:-1]
        for i in range(2, int(max_index)+1):
            download_suc_page(base_url, i, dirname)
            time.sleep(7)
    pass
    

def run():
    args = parse_args()
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    with codecs.open(args.input_path, 'r', 'utf-8') as fin:
        for url in (t.strip() for t in fin):
            if len(url) == 0: continue
            print url
            download_pages(url, args.output_path)
            

def parse_args():
    parser = argparse.ArgumentParser(description='A template for small scripts in puthon3.')
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    return parser.parse_args()


if __name__ == '__main__':
    run()
