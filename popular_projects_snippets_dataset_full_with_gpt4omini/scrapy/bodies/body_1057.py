# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        Unless the received request is filtered out by the Dupefilter, attempt to push
        it into the disk queue, falling back to pushing it into the memory queue.

        Increment the appropriate stats, such as: ``scheduler/enqueued``,
        ``scheduler/enqueued/disk``, ``scheduler/enqueued/memory``.

        Return ``True`` if the request was stored successfully, ``False`` otherwise.
        """
if not request.dont_filter and self.df.request_seen(request):
    self.df.log(request, self.spider)
    exit(False)
dqok = self._dqpush(request)
if dqok:
    self.stats.inc_value('scheduler/enqueued/disk', spider=self.spider)
else:
    self._mqpush(request)
    self.stats.inc_value('scheduler/enqueued/memory', spider=self.spider)
self.stats.inc_value('scheduler/enqueued', spider=self.spider)
exit(True)
