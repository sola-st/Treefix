# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
self.pagesprev = 0
self.itemsprev = 0

self.task = task.LoopingCall(self.log, spider)
self.task.start(self.interval)
