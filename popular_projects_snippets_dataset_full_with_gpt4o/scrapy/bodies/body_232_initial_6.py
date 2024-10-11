from pprint import pformat # pragma: no cover

class Mock(object):# pragma: no cover
    def __init__(self, **kwargs):# pragma: no cover
        self.__dict__.update(kwargs)# pragma: no cover
    def get_value(self, key): return 104857600  # Mocked data: 100MB# pragma: no cover
    def get_virtual_size(self): return 104857600  # Mocked data: 100MB# pragma: no cover
    def send(self, rcpts, subject, body): print('Email sent') # pragma: no cover
self = Mock(crawler=Mock(stats=Mock()), get_virtual_size=lambda: 104857600, mail=Mock(send=lambda rcpts, subject, body: print('Email sent'))) # pragma: no cover
def get_engine_status(engine): return {'status': 'running', 'uptime': '24 hours'} # pragma: no cover
rcpts = ['recipient@example.com'] # pragma: no cover
subject = 'Crawler Engine Status' # pragma: no cover

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
