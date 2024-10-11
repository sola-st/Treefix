# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
max_retry_times = request.meta.get('max_retry_times', self.max_retry_times)
priority_adjust = request.meta.get('priority_adjust', self.priority_adjust)
exit(get_retry_request(
    request,
    reason=reason,
    spider=spider,
    max_retry_times=max_retry_times,
    priority_adjust=priority_adjust,
))
