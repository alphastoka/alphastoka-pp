#!venv/bin/python3.5
# -*- coding: utf-8 -*-
#
import sys
import os
import json

def containKeyword(keyword, text):
    return text.count(keyword)

def containKeywords(keywords, text):
    i = 0
    t = text.lower()
    for x in keywords:
        i += containKeyword(x, t)
    return i

def categorize(input, dictionary):
    data = dictionary
    scorer = {}
    m = 0 #max
    mt = 0 #total
    mk = None

    print('Scoring dictionary')
    for k, v in data.items():
        scorer[k] = containKeywords(v, input)
        if scorer[k] > m:
            m = scorer[k]
            mt += scorer[k]
            mk = k
    return mk, m / float(mt)

if __name__ == '__main__':
    # default command
    dictionary = 'sample/mapper.json'
    with open(dictionary, encoding='utf-8') as mapper:
        print('Parsing dictionary %s' % dictionary)
        data = json.load(mapper)
    mk,conf = categorize('beauty', data)
    if mk is None:
        print("No category")
    else:
        print("category - %s\nconfidence - %.4f" % (mk.encode('utf-8'), conf))