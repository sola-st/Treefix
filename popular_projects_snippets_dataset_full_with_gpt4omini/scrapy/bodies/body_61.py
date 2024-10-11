# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
"""Log the given message at the given log level

        This helper wraps a log call to the logger within the spider, but you
        can use it directly (e.g. Spider.logger.info('msg')) or use any other
        Python logger too.
        """
self.logger.log(level, message, **kw)
