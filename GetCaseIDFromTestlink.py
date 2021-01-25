""" Export Agils test spec info from testlink server 
Dump the name and testlink id of Spec to result file: Record_testlink.csv
Andy Zhang 02/23/2020
V1.0
"""

import testlink
import os
import time
import csv
import openpyxl
import re
import string


csvfile = open('Record_testlink.csv', 'a', newline='')
csv_write = csv.writer(csvfile, dialect='excel')
Record_Time = [time.ctime()]
csv_write.writerow(Record_Time)
csv_write.writerow(['TestlinkID','SPEC name'])

manual = 1  # 手动
automation = 2  # 自动


# 连接test link
url = "http://10.177.40.83:8090/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
key = "b146e6608ddd3532389591707876fa4b" #83 input your key, in testlink--> Account Settings -->API interface
#url = "http://10.177.40.86/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
#key = "b146e6608ddd3532389591707876fa4b"
tlc = testlink.TestlinkAPIClient(url, key)
projectID = tlc.getProjectIDByName('Agilis GVL FW System Test')


#projects = tlc.getProjects()
#top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])

top_suites = tlc.getFirstLevelTestSuitesForTestProject(projectID)
#del 'Basic Smoking Test  ID74980'
for suite in top_suites:
    if suite["name"] == "Basic Smoking Test":
        top_suites.remove(suite)


for suite in top_suites:
    print(suite["name"])
    testcase = tlc.getTestCasesForTestSuite(suite["id"],1,1)

    for i in range(len(testcase)):
#        print(testcase[i]["external_id"], testcase[i]["name"])
        Author = tlc.getTestCaseCustomFieldDesignValue(testcase[i]["external_id"],1,projectID,"Spec_Author",1)
#        print(testcase[i]["external_id"],testcase[i]["name"])
        csv_write.writerow([Author,testcase[i]["external_id"], testcase[i]["name"]])

csvfile.close()





