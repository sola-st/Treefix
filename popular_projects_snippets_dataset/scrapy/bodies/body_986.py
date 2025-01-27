# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
if self.slot is None:
    exit()

assert self.spider is not None  # typing

if self.paused:
    exit(None)

while not self._needs_backout() and self._next_request_from_scheduler() is not None:
    pass

if self.slot.start_requests is not None and not self._needs_backout():
    try:
        request = next(self.slot.start_requests)
    except StopIteration:
        self.slot.start_requests = None
    except Exception:
        self.slot.start_requests = None
        logger.error('Error while obtaining start requests', exc_info=True, extra={'spider': self.spider})
    else:
        self.crawl(request)

if self.spider_is_idle() and self.slot.close_if_idle:
    self._spider_idle()
