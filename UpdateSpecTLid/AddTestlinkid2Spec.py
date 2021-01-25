import traceback
import os
import sys
import time
import csv
import openpyxl
import re
import string
import xlwings as xw

f_Diff = open("Diff.csv","r")
f_D = f_Diff.readlines()
f_Diff.close()

def WriteTIBackToSpec(SpecName,TestlinkID):
    app = xw.App(visible=False,add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    wb = app.books.open(SpecName)
    WB = wb.sheets['Test Overview']
    print(SpecName,TestlinkID)
    WB.range('B15').value= TestlinkID
    wb.save()
    wb.close()
    app.quit()
    
def check_folder(folder,SpecName,TestlinkID):
    list = os.listdir(folder)
    os.chdir(folder)
    for i in range(0,len(list)):
        if os.path.isfile(list[i]): 
            if list[i] == SpecName:
#                print(SpecName)
                WriteTIBackToSpec(SpecName,TestlinkID)

        else:
            if 'Obsolete' in str(list[i]):
                print('Skip Obsolete folder')
            else:
                check_folder(list[i],SpecName,TestlinkID)
    os.chdir('..')
    
    
def main():
    for line in f_D:
        AIN = line.split(',')
        TestlinkID = AIN[1]
        SpecName = AIN[2]
        SpecName = SpecName.replace("\n","")
        folder = "C:\FW_System_Test\GVL\Charlie_Spec"
        check_folder(folder,SpecName,TestlinkID)
    

if __name__ == "__main__":
    main()
    
    
    
    