# Extracted from ./data/repos/scrapy/scrapy/signalmanager.py
"""
        Send a signal, catch exceptions and log them.

        The keyword arguments are passed to the signal handlers (connected
        through the :meth:`connect` method).
        """
kwargs.setdefault('sender', self.sender)
exit(_signal.send_catch_log(signal, **kwargs))
