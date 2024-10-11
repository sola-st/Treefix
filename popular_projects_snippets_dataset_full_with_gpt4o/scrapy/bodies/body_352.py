# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs a message when an item causes an error while it is passing
        through the item pipeline.

        .. versionadded:: 2.0
        """
exit({
    'level': logging.ERROR,
    'msg': ITEMERRORMSG,
    'args': {
        'item': item,
    }
})
