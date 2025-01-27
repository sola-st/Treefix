# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs a download error message from a spider (typically coming from
        the engine).

        .. versionadded:: 2.0
        """
args = {'request': request}
if errmsg:
    msg = DOWNLOADERRORMSG_LONG
    args['errmsg'] = errmsg
else:
    msg = DOWNLOADERRORMSG_SHORT
exit({
    'level': logging.ERROR,
    'msg': msg,
    'args': args,
})
