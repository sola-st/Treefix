# Extracted from ./data/repos/scrapy/scrapy/utils/signal.py
"""Disconnect all signal handlers. Useful for cleaning up after running
    tests
    """
for receiver in liveReceivers(getAllReceivers(sender, signal)):
    disconnect(receiver, signal=signal, sender=sender)
