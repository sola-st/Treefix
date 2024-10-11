# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
if request.meta.get('dont_retry', False):
    exit(response)
if response.status in self.retry_http_codes:
    reason = response_status_message(response.status)
    exit(self._retry(request, reason, spider) or response)
exit(response)
