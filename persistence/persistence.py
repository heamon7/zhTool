import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
import bmemcached
from datetime import datetime
import re

leancloud.init('8scc82ncveedyt6p8ilcz2auzoahzvpu2y800m5075f9flp9', master_key='06vseo6z44ummz0fgv0u6no7vnzqr4fbob0y2mxz6cv47p92')
client1 = bmemcached.Client(('aa41ddf13b914084.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211'),'aa41ddf13b914084','Zhihu7771')
client2 = bmemcached.Client(('b2954ece3d1647b8.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211'),'b2954ece3d1647b8','Zhihu7772')
dbPrime = 97

totalQuestion=0
delRepeatQuestionCount=0
successCount =0

totalCount = int(client2.get('totalCount'))
print "totalCount: %s\n" %str(totalCount)
for questionIndex in range(0,totalCount+1):
    questionId = client2.get(str(questionIndex))
    tableIndex = int(client1.get(str(questionId))[1])

    if tableIndex < 10:
        tableIndexStr = '0' + str(tableIndex)
    else:
        tableIndexStr = str(tableIndex)
    Question = Object.extend('Question' + tableIndexStr)
    query = Query(Question)
    query.equal_to('questionId',str(questionId))
    try:
        questionListRet = query.find()
    except:
        try:
            questionListRet = query.find()
        except:
            try:
                questionListRet = query.find()
            except LeanCloudError,e:
                questionListRet =[]
                print e
                print questionIndex

    if questionListRet:
        questionListRet[0].set('questionIndex',questionIndex)
        try:
            questionListRet[0].save()
            successCount = successCount +1
        except:
            try:
                questionListRet[0].save()
                successCount = successCount +1
            except:
                try:
                    questionListRet[0].save()
                    successCount = successCount +1
                except LeanCloudError,e:
                    print e
                    print questionIndex


    if (questionIndex%10000 ==0):

        print '[%s] the accumulate counts of question finished : %s' % (datetime.now(),str(questionIndex))
        print "the accumulate counts of success question : %s" %str(successCount)
#
print 'Finished All'
