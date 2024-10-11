# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
logger = logging.getLogger(self.name)
exit(logging.LoggerAdapter(logger, {'spider': self}))
