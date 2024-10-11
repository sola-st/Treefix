from pprint import pformat # pragma: no cover

class MockMailer:# pragma: no cover
    def send(self, rcpts, subject, body):# pragma: no cover
        print('Mail sent to:', rcpts)# pragma: no cover
        print('Subject:', subject)# pragma: no cover
        print('Body:', body)# pragma: no cover
 # pragma: no cover
rcpts = ['example@example.com'] # pragma: no cover
subject = 'Crawler Stats' # pragma: no cover
def get_engine_status(engine):# pragma: no cover
    return {# pragma: no cover
        'requests': 10,# pragma: no cover
        'responses': 8,# pragma: no cover
        'exceptions': 2# pragma: no cover
    }# pragma: no cover
 # pragma: no cover
class MockStats:# pragma: no cover
    def get_value(self, key):# pragma: no cover
        return {# pragma: no cover
            'memusage/startup': 512000000,# pragma: no cover
            'memusage/max': 1024000000# pragma: no cover
        }.get(key, 0)# pragma: no cover
 # pragma: no cover
class MockEngine:# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
class MockCrawler:# pragma: no cover
    stats = MockStats()# pragma: no cover
    engine = MockEngine()# pragma: no cover
 # pragma: no cover
type('Mock', (object,), {# pragma: no cover
    'crawler': MockCrawler(),# pragma: no cover
    'get_virtual_size': lambda self: 768000000,# pragma: no cover
    'mail': MockMailer()# pragma: no cover
})() # pragma: no cover

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
