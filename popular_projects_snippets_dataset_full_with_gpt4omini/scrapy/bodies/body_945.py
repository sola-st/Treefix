# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
"""
        When a connection attempt fails, the request cannot be issued.  If no
        result has yet been provided to the result Deferred, provide the
        connection failure reason as an error result.
        """
if self.waiting:
    self.waiting = 0
    # If the connection attempt failed, there is nothing more to
    # disconnect, so just fire that Deferred now.
    self._disconnectedDeferred.callback(None)
    self.deferred.errback(reason)
