from pprint import pformat # pragma: no cover

self = type('Mock', (object,), {# pragma: no cover
    'crawler': type('MockCrawler', (object,), {# pragma: no cover
        'stats': type('MockStats', (object,), {# pragma: no cover
            'get_value': lambda x: 104857600 if x == 'memusage/startup' else 209715200# pragma: no cover
        })()# pragma: no cover
    })(),# pragma: no cover
    'get_virtual_size': lambda: 157286400,# pragma: no cover
    'mail': type('MockMail', (object,), {# pragma: no cover
        'send': lambda rcpts, subject, s: print(f"Mail Sent\nTo: {rcpts}\nSubject: {subject}\n{s}")# pragma: no cover
    })()# pragma: no cover
})() # pragma: no cover
def get_engine_status(engine):# pragma: no cover
    return {'engine': 'active', 'total_requests': 120} # pragma: no cover
rcpts = ['user@example.com'] # pragma: no cover
subject = 'Crawler Engine Status Update' # pragma: no cover

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
