# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""
        Handle the different cases of request's result been a Response or a Failure
        """
if isinstance(result, Response):
    exit(self.spidermw.scrape_response(self.call_spider, result, request, spider))
# else result is a Failure
dfd = self.call_spider(result, request, spider)
exit(dfd.addErrback(self._log_download_errors, result, request, spider))
