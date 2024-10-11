# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
self.crawler = crawler
self.downstream_queue_cls = downstream_queue_cls
self.key = key
self.queues = {}
self.curprio = None
self.init_prios(startprios)
