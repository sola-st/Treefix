from urllib.parse import urlparse # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from collections.abc import Sequence # pragma: no cover
class SequenceExclude(Sequence): # pragma: no cover
    def __init__(self, exclude): # pragma: no cover
        self.exclude = set(exclude) # pragma: no cover
    def __contains__(self, value): # pragma: no cover
        return value not in self.exclude # pragma: no cover
    def __iter__(self): # pragma: no cover
        raise NotImplementedError # pragma: no cover
    def __len__(self): # pragma: no cover
        raise NotImplementedError # pragma: no cover
class UsageError(Exception): # pragma: no cover
    pass # pragma: no cover

opts = type('MockOpts', (object,), {'no_redirect': False, 'spider': None})() # pragma: no cover
args = ['http://example.com'] # pragma: no cover
def is_url(url): # pragma: no cover
    try: # pragma: no cover
        result = urlparse(url) # pragma: no cover
        return all([result.scheme, result.netloc]) # pragma: no cover
    except ValueError: # pragma: no cover
        return False # pragma: no cover
self = type('MockSelf', (object,), {'crawler_process': type('MockCrawlerProcess', (object,), {'spider_loader': type('MockSpiderLoader', (object,), {'load': lambda x: Spider})(), 'crawl': lambda x, y: None, 'start': lambda: None})(), '_print_response': lambda x: None})() # pragma: no cover
def spidercls_for_request(loader, req, default): # pragma: no cover
    return Spider # pragma: no cover
DefaultSpider = Spider # pragma: no cover

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
