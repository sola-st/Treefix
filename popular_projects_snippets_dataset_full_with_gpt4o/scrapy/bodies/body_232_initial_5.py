from pprint import pformat # pragma: no cover

class MockMail:# pragma: no cover
    def send(self, rcpts, subject, s):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockStats:# pragma: no cover
    def get_value(self, key):# pragma: no cover
        return 10485760  # 10MB in bytes# pragma: no cover
# pragma: no cover
class MockEngine:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    stats = MockStats()# pragma: no cover
    engine = MockEngine()# pragma: no cover
def get_engine_status(engine):# pragma: no cover
    return {# pragma: no cover
        'spider_name': 'example_spider',# pragma: no cover
        'engine_status': 'running',# pragma: no cover
        'active_requests': 5,# pragma: no cover
        'pending_requests': 10# pragma: no cover
    } # pragma: no cover
rcpts = ['example@example.com'] # pragma: no cover
subject = 'Crawler Notification' # pragma: no cover

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
