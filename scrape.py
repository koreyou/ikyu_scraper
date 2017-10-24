#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import json
import re

import bs4

class Doc(object):
    def __init__(self):
        self.title = ""
        self.user = ""
        self.user_text = ""
        self.score = 0.0
        self.detailed_score = {}
        self.hotel_text = ""

    def __expr__(self):
        return "{} {}".format(self.score, self.user_text[:20])

    def to_json(self):
        return {
        "title": self.title,
        "user": self.user,
        "user_text": self.user_text,
        "score": self.score,
        "detailed_score": self.detailed_score,
        "hotel_text": self.hotel_text
        }


def run():
    args = parse_args()

    with codecs.open(args.input_path, 'r', 'utf-8') as fin:
        text = fin.read()
    soup = bs4.BeautifulSoup(text, 'html.parser')
    docs = []

    score_re = re.compile(ur"bigiconStar*")
    for review in soup.find_all('div', class_='Wordofmouth_Parts'):
        doc = Doc()
        # TODO: extract score
        for score in review.find_all('div', class_=score_re):
            doc.score = float(score.text.strip())
        # TODO: extract detailed scores
        dscore = {}
        for left in review.find_all('div', class_='left'):
            score_name = ""
            for d in left.find_all('div'):
                if d.span is None:
                    score_name = d.text.strip()
                else:
                    dscore[score_name] = d.text.strip()
        for right in review.find_all('div', class_='right'):
            score_name = ""
            for d in right.find_all('div'):
                if d.span is None:
                    score_name = d.text.strip()
                else:
                    dscore[score_name] = d.text.strip()
        doc.detailed_score = dscore
        # for s in review.find_all('span', class_="score_small"):
        #     print s.text
        # extract user
        for user in review.find_all('div', class_='user'):
            if user.a is not None:
                doc.user = user.a.text
        # extract review text
        for review_text in review.find_all('div', class_='word'):
            doc.user_text = review_text.contents[0].strip()
            for review_return in review_text.find_all('div', class_='word_return'):
                doc.hotel_text = review_return.contents[1].strip()
        docs.append(doc.to_json())
    print json.dumps(docs, indent=4)


def parse_args():
    parser = argparse.ArgumentParser(description='A template for small scripts in puthon3.')
    parser.add_argument('input_path')
    return parser.parse_args()


if __name__ == '__main__':
    run()
