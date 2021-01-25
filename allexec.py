import os 
import datetime
from shutil import copyfile
 
lst=os.listdir(os.getcwd())   
 
#for c in lst:
#    if os.path.isfile(c) and c.endswith('.py') and c.find("AllTest")==-1:    #去掉AllTest.py文件
#        print(c)
#        os.system("python ./%s" % c)  #改动

dateToday = str(datetime.date.today())
FSrc1 = "Diff.csv"
FDst1 = dateToday+FSrc1
FSrc2 = "Record_SPEC.csv"
FDst2 = dateToday+FSrc2
FSrc3 = "Record_testlink.csv"
FDst3 = dateToday+FSrc3

os.rename(FSrc1,FDst1)
os.rename(FSrc2,FDst2)
os.rename(FSrc3,FDst3)

os.system("python ScanSpecFromFloder.py")
os.system("python GetCaseIDFromTestlink.py")
os.system("python Find_testlinkID_diff.py")