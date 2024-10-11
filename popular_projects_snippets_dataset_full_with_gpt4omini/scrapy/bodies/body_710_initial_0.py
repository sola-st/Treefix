from urllib.parse import urlparse # pragma: no cover
from scrapy import Request # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover
from typing import Callable, Dict, Any, List # pragma: no cover

args = ['http://example.com'] # pragma: no cover
def is_url(url): return urlparse(url).scheme in ['http', 'https'] # pragma: no cover
opts = type('Options', (object,), {'no_redirect': False, 'spider': None})() # pragma: no cover
SequenceExclude = type('SequenceExclude', (object,), {'__init__': lambda self, seq: None}) # pragma: no cover
DefaultSpider = type('DefaultSpider', (Spider,), {'name': 'default_spider'}) # pragma: no cover
def spidercls_for_request(spider_loader, request, default_spider): return default_spider # pragma: no cover
class Mock: pass # pragma: no cover
self = type('MockSelf', (object,), { 'crawler_process': CrawlerProcess(), '_print_response': lambda self, response: print(response) })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/fetch.py
from l3.Runtime import _l_
if len(args) != 1 or not is_url(args[0]):
    _l_(10058)

    raise UsageError()
    _l_(10057)
request = Request(args[0], callback=self._print_response,
                  cb_kwargs={"opts": opts}, dont_filter=True)
_l_(10059)
# by default, let the framework handle redirects,
# i.e. command handles all codes expect 3xx
if not opts.no_redirect:
    _l_(10062)

    request.meta['handle_httpstatus_list'] = SequenceExclude(range(300, 400))
    _l_(10060)
else:
    request.meta['handle_httpstatus_all'] = True
    _l_(10061)

spidercls = DefaultSpider
_l_(10063)
spider_loader = self.crawler_process.spider_loader
_l_(10064)
if opts.spider:
    _l_(10067)

    spidercls = spider_loader.load(opts.spider)
    _l_(10065)
else:
    spidercls = spidercls_for_request(spider_loader, request, spidercls)
    _l_(10066)
self.crawler_process.crawl(spidercls, start_requests=lambda: [request])
_l_(10068)
self.crawler_process.start()
_l_(10069)
