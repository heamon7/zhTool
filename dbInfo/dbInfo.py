import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
import bmemcached
from datetime import datetime
import re

leancloud.init('8scc82ncveedyt6p8ilcz2auzoahzvpu2y800m5075f9flp9', master_key='06vseo6z44ummz0fgv0u6no7vnzqr4fbob0y2mxz6cv47p92')
# client1 = bmemcached.Client(('aa41ddf13b914084.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211'),'aa41ddf13b914084','Zhihu7771')
# client2 = bmemcached.Client(('b2954ece3d1647b8.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211'),'b2954ece3d1647b8','Zhihu7772')
dbPrime = 97

totalQuestion=0
delRepeatQuestionCount=0


for tableIndex in range(dbPrime):
    if tableIndex < 10:
        tableIndexStr = '0' + str(tableIndex)
    else:
        tableIndexStr = str(tableIndex)

    Question = Object.extend('Question' + tableIndexStr)
    query = Query(Question)
    query.exists('questionId')
    questionNum = query.count()
    totalQuestion = totalQuestion + questionNum
    #print "questionNums: %s" %str(questionNum)



print "the total counts of questions : %s" %str(totalQuestion)

