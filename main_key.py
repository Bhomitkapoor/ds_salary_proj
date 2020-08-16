# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:53:14 2020

@author: BhomitKapoor
"""


import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/BhomitKapoor/Documents/ds_salary_project/chromedriver"
df = gs.get_jobs("data scientist", 5, False)
df