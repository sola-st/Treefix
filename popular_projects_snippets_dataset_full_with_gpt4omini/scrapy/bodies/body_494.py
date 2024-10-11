# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
for line in buf.rstrip().splitlines():
    self.logger.log(self.log_level, line.rstrip())
