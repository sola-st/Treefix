from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

args = ['http://example.com'] # pragma: no cover
def is_url(url): return url.startswith('http://') or url.startswith('https://') # pragma: no cover
class UsageError(Exception): pass # pragma: no cover
class MockCrawlerProcess(object):  # pragma: no cover
    def __init__(self): self.spider_loader = MockSpiderLoader() # pragma: no cover
    def crawl(self, spidercls, start_requests): pass # pragma: no cover
    def start(self): pass # pragma: no cover
class MockSpiderLoader(object):  # pragma: no cover
    def load(self, spider): return DefaultSpider() # pragma: no cover
class DefaultSpider(Spider): name = 'default_spider' # pragma: no cover
class MockOpts: no_redirect = False; spider = None # pragma: no cover
opts = MockOpts() # pragma: no cover
class SequenceExclude:  # pragma: no cover
    def __init__(self, *args): pass # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._print_response = lambda response: print(response) # pragma: no cover
self.crawler_process = MockCrawlerProcess() # pragma: no cover
def spidercls_for_request(loader, request, default_spider): return default_spider # pragma: no cover

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
