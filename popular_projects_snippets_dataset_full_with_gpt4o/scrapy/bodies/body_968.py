# Extracted from ./data/repos/scrapy/scrapy/core/downloader/middleware.py
if hasattr(mw, 'process_request'):
    self.methods['process_request'].append(mw.process_request)
if hasattr(mw, 'process_response'):
    self.methods['process_response'].appendleft(mw.process_response)
if hasattr(mw, 'process_exception'):
    self.methods['process_exception'].appendleft(mw.process_exception)
