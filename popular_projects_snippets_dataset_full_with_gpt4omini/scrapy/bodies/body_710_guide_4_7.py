from scrapy.http import Request # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover

args = ['http://example.com'] # pragma: no cover
opts = type('MockOptions', (), {'no_redirect': False, 'spider': None})() # pragma: no cover
self = type('MockSelf', (), {'_print_response': lambda response: print('Response:', response), 'crawler_process': CrawlerProcess()})() # pragma: no cover
is_url = lambda url: url.startswith('http://') or url.startswith('https://') # pragma: no cover
DefaultSpider = type('MockSpider', (Spider,), {'name': 'mock_spider'}) # pragma: no cover
spidercls_for_request = lambda spider_loader, request, default_spider: default_spider # pragma: no cover

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
