from pprint import pformat # pragma: no cover

class MockCrawlerStats:# pragma: no cover
    def get_value(self, key):# pragma: no cover
        return 1024 * 1024 * 100  # Returning fixed value for memory size in bytes# pragma: no cover
# pragma: no cover
class MockCrawlerEngine:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.stats = MockCrawlerStats()# pragma: no cover
        self.engine = MockCrawlerEngine()# pragma: no cover
# pragma: no cover
class MockMail:# pragma: no cover
    def send(self, rcpts, subject, body):# pragma: no cover
        print('Sending mail to:', rcpts)# pragma: no cover
        print('Subject:', subject)# pragma: no cover
        print('Body:', body)# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.crawler = MockCrawler()# pragma: no cover
        self.mail = MockMail()# pragma: no cover
    # pragma: no cover
    def get_virtual_size(self):# pragma: no cover
        return 1024 * 1024 * 200  # Returning fixed value for virtual size in bytes# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
def get_engine_status(engine):# pragma: no cover
    return {'status': 'running'}  # Returning a sample status # pragma: no cover
rcpts = ['example@example.com'] # pragma: no cover
subject = 'Crawler Status Update' # pragma: no cover

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
