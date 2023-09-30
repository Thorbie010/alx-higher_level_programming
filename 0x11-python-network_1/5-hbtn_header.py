#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 01:15:59 2023

@author: Jonah Emmanuel
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
