# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
self.signals.send_catch_log(signal=signals.response_downloaded,
                            response=response,
                            request=request,
                            spider=spider)
exit(response)
