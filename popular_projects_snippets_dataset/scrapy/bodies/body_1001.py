# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
def errback(failure: Failure) -> None:
    logger.error(msg, exc_info=failure_to_exc_info(failure), extra={'spider': spider})
exit(errback)
