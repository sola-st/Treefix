# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs an error message from a spider.

        .. versionadded:: 2.0
        """
exit({
    'level': logging.ERROR,
    'msg': SPIDERERRORMSG,
    'args': {
        'request': request,
        'referer': referer_str(request),
    }
})
