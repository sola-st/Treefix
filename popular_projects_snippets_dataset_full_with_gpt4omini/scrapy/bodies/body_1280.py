# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
if failure.type is not IgnoreRequest:
    logger.error("Error downloading %(request)s: %(f_exception)s",
                 {'request': request, 'f_exception': failure.value},
                 exc_info=failure_to_exc_info(failure),
                 extra={'spider': spider})
exit(failure)
