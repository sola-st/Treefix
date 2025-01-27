# Extracted from ./data/repos/scrapy/scrapy/signalmanager.py
"""
        Disconnect all receivers from the given signal.

        :param signal: the signal to disconnect from
        :type signal: object
        """
kwargs.setdefault('sender', self.sender)
exit(_signal.disconnect_all(signal, **kwargs))
