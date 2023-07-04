#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed July 04 17:43:34 2023

@author: Jonah Emmanuel
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
