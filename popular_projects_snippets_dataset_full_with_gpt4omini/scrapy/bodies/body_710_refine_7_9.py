from urllib.parse import urlparse # pragma: no cover
from scrapy import Request # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.utils.spider import spidercls_for_request # pragma: no cover

args = ['http://example.com'] # pragma: no cover
def is_url(url): return urlparse(url).scheme in ('http', 'https') # pragma: no cover
opts = type('Mock', (), {'no_redirect': False, 'spider': None})() # pragma: no cover
SequenceExclude = type('Mock', (), {'__call__': lambda self, x: x})() # pragma: no cover
self = type('Mock', (), {'_print_response': lambda response: print(response), 'crawler_process': type('Mock', (), {'crawl': lambda cls, start_requests: None, 'start': lambda: None, 'spider_loader': type('Mock', (), {'load': lambda spider: DefaultSpider})()})()})() # pragma: no cover

from urllib.parse import urlparse # pragma: no cover
from scrapy import Request # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover

args = ['http://example.com'] # pragma: no cover
def is_url(url): return urlparse(url).scheme in ('http', 'https') # pragma: no cover
opts = type('Mock', (), {'no_redirect': False, 'spider': None})() # pragma: no cover
SequenceExclude = type('Mock', (), {'__init__': lambda self, seq: setattr(self, 'seq', seq)}) # pragma: no cover
class DefaultSpider(Spider): name = 'default_spider' # pragma: no cover
def spidercls_for_request(loader, request, default_cls): return default_cls # pragma: no cover
self = type('Mock', (), {'_print_response': lambda response: print(response), 'crawler_process': CrawlerProcess()})() # pragma: no cover

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
