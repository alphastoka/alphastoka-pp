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
    scorer = {}
    total = 0

    # iterate and score dictionary
    for k, v in dictionary.items():
        scorer[k] = containKeywords(v, input)
        total += scorer[k]

    # get confidence value
    for k, v in scorer.items():
        scorer[k] = scorer[k] / float(total)

    return scorer