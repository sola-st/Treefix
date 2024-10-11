from scrapy.crawler import Crawler # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover

crawler_or_spidercls = Spider # pragma: no cover
Spider = type('MockSpider', (Spider,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'create_crawler': lambda cls, spider: Crawler(spider), '_crawl': lambda cls, crawler, *args, **kwargs: 'crawl finished'})() # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

from scrapy.crawler import Crawler # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover

crawler_or_spidercls = type('MockSpider', (Spider,), {}) # pragma: no cover
class MockSelf:# pragma: no cover
    def create_crawler(self, spider_cls):# pragma: no cover
        return Crawler(spider_cls)# pragma: no cover
    def _crawl(self, crawler, *args, **kwargs):# pragma: no cover
        return 'Crawling completed' # pragma: no cover
self = MockSelf() # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/crawler.py
from l3.Runtime import _l_
"""
        Run a crawler with the provided arguments.

        It will call the given Crawler's :meth:`~Crawler.crawl` method, while
        keeping track of it so it can be stopped later.

        If ``crawler_or_spidercls`` isn't a :class:`~scrapy.crawler.Crawler`
        instance, this method will try to create one using this parameter as
        the spider class given to it.

        Returns a deferred that is fired when the crawling is finished.

        :param crawler_or_spidercls: already created crawler, or a spider class
            or spider's name inside the project to create it
        :type crawler_or_spidercls: :class:`~scrapy.crawler.Crawler` instance,
            :class:`~scrapy.spiders.Spider` subclass or string

        :param args: arguments to initialize the spider

        :param kwargs: keyword arguments to initialize the spider
        """
if isinstance(crawler_or_spidercls, Spider):
    _l_(9351)

    raise ValueError(
        'The crawler_or_spidercls argument cannot be a spider object, '
        'it must be a spider class (or a Crawler object)')
    _l_(9350)
crawler = self.create_crawler(crawler_or_spidercls)
_l_(9352)
aux = self._crawl(crawler, *args, **kwargs)
_l_(9353)
exit(aux)
