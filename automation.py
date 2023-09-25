# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 00:36:43 2023

@author: Kun-Yuan
"""
import os

with open("./block.txt") as f:
    #print(f.read().format("someone","stuuuuudent","shit"))
    block = f.read()

blocks_en = ""
blocks_zh = ""
role_en = {"POSTDOC": "POST DOCTORAL RESEARCH FELLOW",
           "PHD": "PHD STUDENT",
           "MS" : "MASTER STUDENT",
           "BS" : "COLLEGE STUDENT"
           }
role_zh = {"POSTDOC": "博士後研究",
           "PHD": "光電所博班",
           "MS" : "碩士班",
           "BS" : "大學部專題"
           }
level = {"POSTDOC": 0,
         "PHD": 1,
         "MS" : 10,
         "BS" : 100
        }

def rule(s):
    title, year, name_en, name_zh = s[:s.index('.')].split('_')
    return level[title]+int(year)

for file_name in sorted(os.listdir("./assets/img/students/"),key=rule):
    print(file_name)
    title, year, name_en, name_zh = file_name[:file_name.index('.')].split('_')
    blocks_en += block.format(file_name, role_en[title], name_en)
    blocks_zh += block.format(file_name, role_zh[title], name_zh)

with open("./blocks_en.txt", 'w') as f:
    f.write(blocks_en)
with open("./blocks_zh.txt", 'w') as f:
    f.write(blocks_zh)