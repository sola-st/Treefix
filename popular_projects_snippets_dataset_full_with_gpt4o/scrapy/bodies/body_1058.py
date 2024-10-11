# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        Return a :class:`~scrapy.http.Request` object from the memory queue,
        falling back to the disk queue if the memory queue is empty.
        Return ``None`` if there are no more enqueued requests.

        Increment the appropriate stats, such as: ``scheduler/dequeued``,
        ``scheduler/dequeued/disk``, ``scheduler/dequeued/memory``.
        """
request = self.mqs.pop()
if request is not None:
    self.stats.inc_value('scheduler/dequeued/memory', spider=self.spider)
else:
    request = self._dqpop()
    if request is not None:
        self.stats.inc_value('scheduler/dequeued/disk', spider=self.spider)
if request is not None:
    self.stats.inc_value('scheduler/dequeued', spider=self.spider)
exit(request)
