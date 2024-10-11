# Extracted from ./data/repos/scrapy/scrapy/middleware.py
if hasattr(mw, 'open_spider'):
    self.methods['open_spider'].append(mw.open_spider)
if hasattr(mw, 'close_spider'):
    self.methods['close_spider'].appendleft(mw.close_spider)
