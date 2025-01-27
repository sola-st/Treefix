# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
"""Called per item when all media requests has been processed"""
if self.LOG_FAILED_RESULTS:
    for ok, value in results:
        if not ok:
            logger.error(
                '%(class)s found errors processing %(item)s',
                {'class': self.__class__.__name__, 'item': item},
                exc_info=failure_to_exc_info(value),
                extra={'spider': info.spider}
            )
exit(item)
