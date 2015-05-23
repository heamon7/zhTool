
import bmemcached
import numpy as np
import csv
from datetime import datetime
import re

client2 = bmemcached.Client('7030b81da1324743.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211','7030b81da1324743','Zhihucache2')
client3 = bmemcached.Client('92a2b309a9f145d2.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211','92a2b309a9f145d2','Zhihucache3')
dbPrime = 97
questionIdSet=set()
questionInfoList =[]

totalCount = int(client2.get('totalCount'))
print "totalCount: %s\n" %str(totalCount)

for questionIndex in range(0,totalCount+1):
    questionIdSet.add(int(client2.get(str(questionIndex))[0]))

print "length of  questionIdSet: %s" %str(len(questionIdSet))

with open('/home/heamon7/Project/questionIdCSV.csv','w') as questionIdCSV:
    # fieldnames = ['questionId','isTopQuestion','questionAnswerCount','questionFollowerCount']
    questionInfoWriter = csv.writer(questionIdCSV,delimiter=' ')
    for questionInfo in questionIdSet:
        questionInfoWriter.writerow([questionInfo])

for questionId in questionIdSet:
    res =client3.get(str(questionId))
    if res :
       res = np.array(res)[[1,3,4]]
       questionInfoList.append(np.insert(res,0,int(questionId)))
    else :
        pass

print "length of  questionInfoList: %s" %str(len(questionInfoList))



with open('/home/heamon7/Project/questionInfoCSV.csv','w') as questionInfoCSV:
    # fieldnames = ['questionId','isTopQuestion','questionAnswerCount','questionFollowerCount']
    questionInfoWriter = csv.writer(questionInfoCSV,delimiter=' ')
    for questionInfo in questionInfoList:
        questionInfoWriter.writerow(questionInfo)




print 'Finished All'