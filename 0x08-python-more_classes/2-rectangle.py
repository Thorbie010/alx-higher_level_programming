#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 03 2023

@author: Jonah Emmanuel
"""


class Rectangle:
    """class Rectangle that defines a rectangle figure

    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        self.width = width
        self.height = height
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Calculate area of the rectangle

        Returns:
            area (int): The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate perimeter of the rectangle

        Returns:
            perimeter (int): The perimeter of the rectangle
        """
        if self.__width == 0:
            perimeter = 0
        elif self.__height == 0:
            perimeter = 0
        else:
            return 2 * (self.__height + self.__width)
