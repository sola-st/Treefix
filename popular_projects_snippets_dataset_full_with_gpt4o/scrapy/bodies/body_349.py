# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs a message when the crawler finds a webpage."""
request_flags = f' {str(request.flags)}' if request.flags else ''
response_flags = f' {str(response.flags)}' if response.flags else ''
exit({
    'level': logging.DEBUG,
    'msg': CRAWLEDMSG,
    'args': {
        'status': response.status,
        'request': request,
        'request_flags': request_flags,
        'referer': referer_str(request),
        'response_flags': response_flags,
        # backward compatibility with Scrapy logformatter below 1.4 version
        'flags': response_flags
    }
})
