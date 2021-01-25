""" Compare Record_SPEC.csv and Record_testlink.csv
Find the Spec testlink id diff for testlink server, record it to diff.csv
Andy Zhang 02/23/2020
V1.0
"""


import traceback
import os
import sys
import time
import csv
import openpyxl
import re
import string


f_Git = open("Record_SPEC.csv","r")
f_TC = open("Record_testlink.csv","r")

f_G = f_Git.readlines()
f_T = f_TC.readlines()


f_Git.close()
f_TC.close()


outfile = open("Diff.csv","w")
outfile.write("This is different, check Spec please: \n")

for i in f_T:
    print(i)

    for j in f_G:
#        print(j)
#        ret = re.findall(j,i,flags=re.IGNORECASE)
#        if i not in f_G:
        ret = i.find(j)
        if ret != -1:
            break
    if ret == -1:
        outfile.write(i)


outfile.close()
