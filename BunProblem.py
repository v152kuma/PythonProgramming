# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:02:40 2019

@author: vyadav44
"""

bunprice=float(input("Enter the price of single bun: "))

print("The price of one bun is " )
print(bunprice)

wallet=float(input("Please enter the amount of money you have in your pocket : "))

print("Number of buns you can buy is ")
print(wallet//bunprice)