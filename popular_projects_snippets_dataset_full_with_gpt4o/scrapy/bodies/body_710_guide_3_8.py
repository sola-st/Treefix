from scrapy.http import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from urllib.parse import urlparse # pragma: no cover

args = ['http://example.com'] # pragma: no cover
def is_url(url): # pragma: no cover
    try: # pragma: no cover
        result = urlparse(url) # pragma: no cover
        return all([result.scheme, result.netloc]) # pragma: no cover
    except ValueError: # pragma: no cover
        return False # pragma: no cover
opts = type('Opts', (object,), {'no_redirect': False, 'spider': None})() # pragma: no cover
class SequenceExclude: # pragma: no cover
    def __init__(self, exclude_range): # pragma: no cover
        self.exclude_range = exclude_range # pragma: no cover
    def __contains__(self, item): # pragma: no cover
        return item not in self.exclude_range # pragma: no cover
class DefaultSpider(Spider): # pragma: no cover
    name = 'default' # pragma: no cover
def spidercls_for_request(loader, request, default): # pragma: no cover
    return default # pragma: no cover
class MockCrawlerProcess(CrawlerProcess): # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__() # pragma: no cover
        self.spider_loader = type('SpiderLoader', (object,), {'load': lambda self, name: DefaultSpider})() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_print_response': lambda x: None, # pragma: no cover
    'crawler_process': MockCrawlerProcess() # pragma: no cover
}) # pragma: no cover

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
