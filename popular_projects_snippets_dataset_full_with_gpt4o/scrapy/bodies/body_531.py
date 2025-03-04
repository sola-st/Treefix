# Extracted from ./data/repos/scrapy/scrapy/utils/ossignal.py
"""Install the given function as a signal handler for all common shutdown
    signals (such as SIGINT, SIGTERM, etc). If override_sigint is ``False`` the
    SIGINT handler won't be install if there is already a handler in place
    (e.g.  Pdb)
    """
from twisted.internet import reactor
reactor._handleSignals()
signal.signal(signal.SIGTERM, function)
if signal.getsignal(signal.SIGINT) == signal.default_int_handler or override_sigint:
    signal.signal(signal.SIGINT, function)
# Catch Ctrl-Break in windows
if hasattr(signal, 'SIGBREAK'):
    signal.signal(signal.SIGBREAK, function)
