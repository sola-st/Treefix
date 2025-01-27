# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
assert self.slot is not None  # typing
assert self.spider is not None  # typing

request = self.slot.scheduler.next_request()
if request is None:
    exit(None)

d = self._download(request, self.spider)
d.addBoth(self._handle_downloader_output, request)
d.addErrback(lambda f: logger.info('Error while handling downloader output',
                                   exc_info=failure_to_exc_info(f),
                                   extra={'spider': self.spider}))
d.addBoth(lambda _: self.slot.remove_request(request))
d.addErrback(lambda f: logger.info('Error while removing request from slot',
                                   exc_info=failure_to_exc_info(f),
                                   extra={'spider': self.spider}))
slot = self.slot
d.addBoth(lambda _: slot.nextcall.schedule())
d.addErrback(lambda f: logger.info('Error while scheduling new request',
                                   exc_info=failure_to_exc_info(f),
                                   extra={'spider': self.spider}))
exit(d)
