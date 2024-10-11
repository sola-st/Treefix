# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
if self.handle_httpstatus_list:
    request.meta['handle_httpstatus_list'] = self.handle_httpstatus_list
else:
    request.meta['handle_httpstatus_all'] = True
