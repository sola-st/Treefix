# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/httperror.py
if isinstance(exception, HttpError):
    spider.crawler.stats.inc_value('httperror/response_ignored_count')
    spider.crawler.stats.inc_value(
        f'httperror/response_ignored_status_count/{response.status}'
    )
    logger.info(
        "Ignoring response %(response)r: HTTP status code is not handled or not allowed",
        {'response': response}, extra={'spider': spider},
    )
    exit([])
