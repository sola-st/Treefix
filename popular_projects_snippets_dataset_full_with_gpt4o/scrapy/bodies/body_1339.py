# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
ex_class = global_object_name(exception.__class__)
self.stats.inc_value('downloader/exception_count', spider=spider)
self.stats.inc_value(f'downloader/exception_type_count/{ex_class}', spider=spider)
