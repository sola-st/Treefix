# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
self.handle_httpstatus_list = None
if allow_redirects:
    self.handle_httpstatus_list = SequenceExclude(range(300, 400))
