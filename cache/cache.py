import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
import bmemcached
from datetime import datetime
import re

leancloud.init('8scc82ncveedyt6p8ilcz2auzoahzvpu2y800m5075f9flp9', master_key='06vseo6z44ummz0fgv0u6no7vnzqr4fbob0y2mxz6cv47p92')
client = bmemcached.Client(('d69c4508ccc94dc4.m.cnbjalinu16pub001.ocs.aliyuncs.com:11211'),'d69c4508ccc94dc4')
dbPrime = 97


for tableIndex in range(dbPrime):
    if tableIndex < 10:
        tableIndexStr = '0' + str(tableIndex)
    else:
        tableIndexStr = str(tableIndex)

    Question = Object.extend('Question' + tableIndexStr)
    query = Query(Question)
    query.exists('questionLinkHref')
    #curTime = datetime.now()
    #query.less_than('createdAt',curTime)
    questionNum = query.count()
    #print "questionNums: %s" %str(questionNum)
    queryLimit = 700
    queryTimes = questionNum/queryLimit + 1
    urls = []
    for index in range(queryTimes):
        query = Query(Question)
        #query.less_than('createdAt',Question)
        query.exists('questionLinkHref')
        query.descending('createdAt')
        query.limit(queryLimit)
        query.skip(index*queryLimit)
        #query.select('questionLinkHref')
        quesRet = query.find()

        for ques in quesRet:
            quesCacheList =[]
            quesCacheList.append(ques.get('tableIndex'))
            quesCacheList.append(ques.get('answerCount'))
            if ques.get('isTopQuestion') == 'true':
                quesCacheList.append(1)
            else:
                quesCacheList.append(0)
            quesCacheList.append(int(ques.get('quesTimestamp')))
            questionIdStr = re.split('/question/',str)[1]
            try:
                ques.set('questionId',questionIdStr)
                ques.save()
            except LeanCloudError,e:
                print e
            client.set(questionIdStr,quesCacheList)
            client.incr('totalCount',1)

    print 'table finished: %s\n' % tableIndexStr

print 'Finished All'