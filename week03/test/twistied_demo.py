from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor
from time import sleep

def a(*args,**kwargs):
    
    print('a开始:',args)

def b(*args):
    print('b开始:',args)

@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(a(url))
    d.addCallback(b(url))
    yield d

def stop(*args, **kwargs):
    reactor.stop()

urls = ['http://www.baidu.com','http://www.sougou.com']
li = []

for u in urls:
    ret = start(u)
    li.append(ret)
print(li)

d = defer.DeferredList(li)
d.addBoth(stop)
reactor.run()