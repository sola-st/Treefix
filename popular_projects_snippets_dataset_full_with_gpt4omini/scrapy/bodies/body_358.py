# Extracted from ./data/repos/scrapy/scrapy/signalmanager.py
"""
        Disconnect a receiver function from a signal. This has the
        opposite effect of the :meth:`connect` method, and the arguments
        are the same.
        """
kwargs.setdefault('sender', self.sender)
exit(dispatcher.disconnect(receiver, signal, **kwargs))
