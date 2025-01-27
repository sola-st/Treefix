# Extracted from ./data/repos/scrapy/scrapy/extensions/debug.py
try:
    signal.signal(signal.SIGUSR2, self._enter_debugger)
except AttributeError:
    # win32 platforms don't support SIGUSR signals
    pass
