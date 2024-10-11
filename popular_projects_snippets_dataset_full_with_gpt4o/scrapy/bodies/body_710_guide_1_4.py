from scrapy.http import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from unittest.mock import Mock # pragma: no cover
from urllib.parse import urlparse # pragma: no cover

args = ['invalid_url'] # pragma: no cover
def is_url(url): parsed = urlparse(url); return bool(parsed.scheme and parsed.netloc) # pragma: no cover
opts = Mock() # pragma: no cover
opts.no_redirect = False # pragma: no cover
opts.spider = 'some_spider' # pragma: no cover
SequenceExclude = lambda r: type('SequenceExclude', (object,), {'__contains__': lambda self, item: item not in r})() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._print_response = Mock() # pragma: no cover
self.crawler_process = CrawlerProcess() # pragma: no cover
self.crawler_process.spider_loader = type('Mock', (), {'load': lambda name: Spider})() # pragma: no cover
def spidercls_for_request(loader, request, default): return default # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/fetch.py
from l3.Runtime import _l_
if len(args) != 1 or not is_url(args[0]):
    _l_(21469)

    raise UsageError()
    _l_(21468)
request = Request(args[0], callback=self._print_response,
                  cb_kwargs={"opts": opts}, dont_filter=True)
_l_(21470)
# by default, let the framework handle redirects,
# i.e. command handles all codes expect 3xx
if not opts.no_redirect:
    _l_(21473)

    request.meta['handle_httpstatus_list'] = SequenceExclude(range(300, 400))
    _l_(21471)
else:
    request.meta['handle_httpstatus_all'] = True
    _l_(21472)

spidercls = DefaultSpider
_l_(21474)
spider_loader = self.crawler_process.spider_loader
_l_(21475)
if opts.spider:
    _l_(21478)

    spidercls = spider_loader.load(opts.spider)
    _l_(21476)
else:
    spidercls = spidercls_for_request(spider_loader, request, spidercls)
    _l_(21477)
self.crawler_process.crawl(spidercls, start_requests=lambda: [request])
_l_(21479)
self.crawler_process.start()
_l_(21480)
