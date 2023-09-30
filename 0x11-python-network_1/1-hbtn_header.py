#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 01:15:59 2023

@author: Jonah Emmanuel
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
