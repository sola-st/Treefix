# Extracted from ./data/repos/scrapy/scrapy/signalmanager.py
"""
        Connect a receiver function to a signal.

        The signal can be any object, although Scrapy comes with some
        predefined signals that are documented in the :ref:`topics-signals`
        section.

        :param receiver: the function to be connected
        :type receiver: collections.abc.Callable

        :param signal: the signal to connect to
        :type signal: object
        """
kwargs.setdefault('sender', self.sender)
exit(dispatcher.connect(receiver, signal, **kwargs))
