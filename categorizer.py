#!venv/bin/python3.5
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

# input - input text to categorize
# dict - python dictionary of form { categoryName: [keywords] }
# return - key-value of categoryName and scoring in percent dictionary. For example, { categoryName: 1.000 }
def categorize(input, dictionary):
    scorer = {}
    total = 0

    # iterate and score dictionary
    for k, v in dictionary.items():
        score = containKeywords(v, input)
        if score != 0:
            scorer[k] = score
            total += score

    # get confidence value
    for k, v in scorer.items():
        scorer[k] = scorer[k] / float(total)

    return scorer

# entry - mongodb instagram data entry
# dict - python dictionary of form { categoryName: [array_of_keywords] }
# return - modified entry with entry['category'] = [array_of_keywords]
def instagram(entry, dictionary=None):
    x = ''
    # get dict from default json if not specified
    if dictionary is None:
        dictionary = get_dict('sample/mapper.json')

    # only if biography exist
    if isinstance(entry['biography'], str):
        x += entry['biography']

    # concat all media captions
    for n in entry['media']['nodes']:
        x += n['caption']

    # categorize 
    z = categorize(x, dictionary).keys()
    entry['category'] = z
    return entry

# get dict from json
def get_dict(dictionaryJson):
    with open(dictionaryJson) as f:
        return json.load(f)