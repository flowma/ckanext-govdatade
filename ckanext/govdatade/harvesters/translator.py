#!/bin/env python
import ConfigParser
import json
import os
import urllib2


def translate_groups(groups, source_name):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')
    url = config.get('URLs', 'categories') + source_name + '2deutschland.json'
    json_string = urllib2.urlopen(url).read()
    group_dict = json.loads(json_string)

    result = []
    for group in groups:
        if group in group_dict:
            result = result + group_dict[group]
    return result
