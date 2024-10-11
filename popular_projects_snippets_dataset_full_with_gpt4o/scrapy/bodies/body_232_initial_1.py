from pprint import pformat # pragma: no cover

class MockMail:# pragma: no cover
    def send(self, recipients, subject, body):# pragma: no cover
        pass # pragma: no cover
class MockCrawlerEngine:# pragma: no cover
    pass # pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.stats = {# pragma: no cover
            'memusage/startup': 10485760,# pragma: no cover
            'memusage/max': 20971520# pragma: no cover
        }# pragma: no cover
        self.engine = MockCrawlerEngine() # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'crawler': MockCrawler(),# pragma: no cover
    'get_virtual_size': lambda self: 31457280,# pragma: no cover
    'mail': MockMail()# pragma: no cover
})() # pragma: no cover
def get_engine_status(engine):# pragma: no cover
    return {'status': 'running', 'item_count': 100} # pragma: no cover
rcpts = ['example@example.com'] # pragma: no cover
subject = 'Crawler Memory Usage Report' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
from l3.Runtime import _l_
"""send notification mail with some additional useful info"""
stats = self.crawler.stats
_l_(20983)
s = f"Memory usage at engine startup : {stats.get_value('memusage/startup')/1024/1024}M\r\n"
_l_(20984)
s += f"Maximum memory usage          : {stats.get_value('memusage/max')/1024/1024}M\r\n"
_l_(20985)
s += f"Current memory usage          : {self.get_virtual_size()/1024/1024}M\r\n"
_l_(20986)

s += "ENGINE STATUS ------------------------------------------------------- \r\n"
_l_(20987)
s += "\r\n"
_l_(20988)
s += pformat(get_engine_status(self.crawler.engine))
_l_(20989)
s += "\r\n"
_l_(20990)
self.mail.send(rcpts, subject, s)
_l_(20991)
