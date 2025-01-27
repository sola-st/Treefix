# Extracted from ./data/repos/scrapy/scrapy/shell.py
if is_asyncio_reactor_installed():
    # set the asyncio event loop for the current thread
    event_loop_path = self.crawler.settings['ASYNCIO_EVENT_LOOP']
    set_asyncio_event_loop(event_loop_path)
spider = self._open_spider(request, spider)
d = _request_deferred(request)
d.addCallback(lambda x: (x, spider))
self.crawler.engine.crawl(request)
exit(d)
