# Extracted from ./data/repos/scrapy/scrapy/shell.py
"""Wrap a request inside a Deferred.

    This function is harmful, do not use it until you know what you are doing.

    This returns a Deferred whose first pair of callbacks are the request
    callback and errback. The Deferred also triggers when the request
    callback/errback is executed (i.e. when the request is downloaded)

    WARNING: Do not call request.replace() until after the deferred is called.
    """
request_callback = request.callback
request_errback = request.errback

def _restore_callbacks(result):
    request.callback = request_callback
    request.errback = request_errback
    exit(result)

d = defer.Deferred()
d.addBoth(_restore_callbacks)
if request.callback:
    d.addCallbacks(request.callback, request.errback)

request.callback, request.errback = d.callback, d.errback
exit(d)
