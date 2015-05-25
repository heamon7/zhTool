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
    query.equal_to('flag',3)


    questionNum = query.count()
    #print "questionNums: %s" %str(questionNum)
    queryLimit = 700
    queryTimes = questionNum/queryLimit + 1

    for index in range(queryTimes):
        query = Query(Question)
        #query.less_than('createdAt',Question)
        query.equal_to('flag',3)
        query.descending('createdAt')
        query.limit(queryLimit)
        # query.skip(index*queryLimit)
        quesRet = query.find()
        for ques in quesRet:
            try:
                ques.destroy()
            except:
                try:
                    ques.destroy()
                except:
                    try:
                        ques.destroy()
                    except LeanCloudError,e:
                        print e
                        print ques.get('questionId')

            delRepeatQuestionCount =delRepeatQuestionCount+1

    print '[%s] table finished with tableIndexStr: %s' % (datetime.now(),str(tableIndexStr))
    print "the accumulate counts of del repeat question : %s" %str(delRepeatQuestionCount)
#
print 'Finished All'
