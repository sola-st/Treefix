# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
if (
    isinstance(exception, self.EXCEPTIONS_TO_RETRY)
    and not request.meta.get('dont_retry', False)
):
    exit(self._retry(request, exception, spider))
