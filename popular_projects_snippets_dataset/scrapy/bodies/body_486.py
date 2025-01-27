# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
if any(record.name.startswith(logger + '.') for logger in self.loggers):
    record.name = record.name.split('.', 1)[0]
exit(True)
