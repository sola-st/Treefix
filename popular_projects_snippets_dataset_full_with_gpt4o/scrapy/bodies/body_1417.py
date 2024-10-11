# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
exit(ScrapyPriorityQueue(
    self.crawler,
    self.downstream_queue_cls,
    self.key + '/' + _path_safe(slot),
    startprios,
))
