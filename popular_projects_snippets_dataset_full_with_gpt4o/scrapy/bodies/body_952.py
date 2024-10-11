# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
delay = settings.getfloat('DOWNLOAD_DELAY')
if hasattr(spider, 'download_delay'):
    delay = spider.download_delay

if hasattr(spider, 'max_concurrent_requests'):
    concurrency = spider.max_concurrent_requests

exit((concurrency, delay))
