# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
spider.crawler.stats.inc_value('file_count', spider=spider)
spider.crawler.stats.inc_value(f'file_status_count/{status}', spider=spider)
