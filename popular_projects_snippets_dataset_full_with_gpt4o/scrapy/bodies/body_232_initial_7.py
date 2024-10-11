from pprint import pformat # pragma: no cover

self = type('Mock', (object,), {'crawler': type('MockCrawler', (object,), {'stats': type('MockStats', (object,), {'get_value': lambda self, key: 104857600})()})(), 'get_virtual_size': lambda self: 104857600, 'mail': type('MockMail', (object,), {'send': lambda self, rcpts, subject, body: print(f'Mail sent to {rcpts} with subject "{subject}"')})()})() # pragma: no cover
get_engine_status = lambda engine: {'engine': 'active', 'spiders': 5} # pragma: no cover
rcpts = ['example@example.com', 'admin@example.com'] # pragma: no cover
subject = 'Crawler Memory and Engine Status' # pragma: no cover

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
