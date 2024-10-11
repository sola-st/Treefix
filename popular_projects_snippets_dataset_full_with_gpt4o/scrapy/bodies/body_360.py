# Extracted from ./data/repos/scrapy/scrapy/signalmanager.py
"""
        Like :meth:`send_catch_log` but supports returning
        :class:`~twisted.internet.defer.Deferred` objects from signal handlers.

        Returns a Deferred that gets fired once all signal handlers
        deferreds were fired. Send a signal, catch exceptions and log them.

        The keyword arguments are passed to the signal handlers (connected
        through the :meth:`connect` method).
        """
kwargs.setdefault('sender', self.sender)
exit(_signal.send_catch_log_deferred(signal, **kwargs))
