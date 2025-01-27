# Extracted from ./data/repos/scrapy/scrapy/shell.py
from twisted.internet import reactor
if isinstance(request_or_url, Request):
    request = request_or_url
else:
    url = any_to_uri(request_or_url)
    request = Request(url, dont_filter=True, **kwargs)
    if redirect:
        request.meta['handle_httpstatus_list'] = SequenceExclude(range(300, 400))
    else:
        request.meta['handle_httpstatus_all'] = True
response = None
try:
    response, spider = threads.blockingCallFromThread(
        reactor, self._schedule, request, spider)
except IgnoreRequest:
    pass
self.populate_vars(response, request, spider)
