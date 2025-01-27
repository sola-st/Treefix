# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
"""
    Returns a new :class:`~scrapy.Request` object to retry the specified
    request, or ``None`` if retries of the specified request have been
    exhausted.

    For example, in a :class:`~scrapy.Spider` callback, you could use it as
    follows::

        def parse(self, response):
            if not response.text:
                new_request_or_none = get_retry_request(
                    response.request,
                    spider=self,
                    reason='empty',
                )
                return new_request_or_none

    *spider* is the :class:`~scrapy.Spider` instance which is asking for the
    retry request. It is used to access the :ref:`settings <topics-settings>`
    and :ref:`stats <topics-stats>`, and to provide extra logging context (see
    :func:`logging.debug`).

    *reason* is a string or an :class:`Exception` object that indicates the
    reason why the request needs to be retried. It is used to name retry stats.

    *max_retry_times* is a number that determines the maximum number of times
    that *request* can be retried. If not specified or ``None``, the number is
    read from the :reqmeta:`max_retry_times` meta key of the request. If the
    :reqmeta:`max_retry_times` meta key is not defined or ``None``, the number
    is read from the :setting:`RETRY_TIMES` setting.

    *priority_adjust* is a number that determines how the priority of the new
    request changes in relation to *request*. If not specified, the number is
    read from the :setting:`RETRY_PRIORITY_ADJUST` setting.

    *logger* is the logging.Logger object to be used when logging messages

    *stats_base_key* is a string to be used as the base key for the
    retry-related job stats
    """
settings = spider.crawler.settings
stats = spider.crawler.stats
retry_times = request.meta.get('retry_times', 0) + 1
if max_retry_times is None:
    max_retry_times = request.meta.get('max_retry_times')
    if max_retry_times is None:
        max_retry_times = settings.getint('RETRY_TIMES')
if retry_times <= max_retry_times:
    logger.debug(
        "Retrying %(request)s (failed %(retry_times)d times): %(reason)s",
        {'request': request, 'retry_times': retry_times, 'reason': reason},
        extra={'spider': spider}
    )
    new_request: Request = request.copy()
    new_request.meta['retry_times'] = retry_times
    new_request.dont_filter = True
    if priority_adjust is None:
        priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
    new_request.priority = request.priority + priority_adjust

    if callable(reason):
        reason = reason()
    if isinstance(reason, Exception):
        reason = global_object_name(reason.__class__)

    stats.inc_value(f'{stats_base_key}/count')
    stats.inc_value(f'{stats_base_key}/reason_count/{reason}')
    exit(new_request)
stats.inc_value(f'{stats_base_key}/max_reached')
logger.error(
    "Gave up retrying %(request)s (failed %(retry_times)d times): "
    "%(reason)s",
    {'request': request, 'retry_times': retry_times, 'reason': reason},
    extra={'spider': spider},
)
exit(None)
