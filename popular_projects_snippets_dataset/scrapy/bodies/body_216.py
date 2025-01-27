# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
if self.task and self.task.running:
    self.task.stop()
