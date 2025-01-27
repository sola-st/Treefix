# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
exit(create_instance(
    self.downstream_queue_cls,
    None,
    self.crawler,
    self.key + '/' + str(key),
))
