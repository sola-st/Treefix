# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
self._encoding = encoding  # this one has to be set first
self.method = str(method).upper()
self._set_url(url)
self._set_body(body)
if not isinstance(priority, int):
    raise TypeError(f"Request priority not an integer: {priority!r}")
self.priority = priority

if callback is not None and not callable(callback):
    raise TypeError(f'callback must be a callable, got {type(callback).__name__}')
if errback is not None and not callable(errback):
    raise TypeError(f'errback must be a callable, got {type(errback).__name__}')
self.callback = callback
self.errback = errback

self.cookies = cookies or {}
self.headers = Headers(headers or {}, encoding=encoding)
self.dont_filter = dont_filter

self._meta = dict(meta) if meta else None
self._cb_kwargs = dict(cb_kwargs) if cb_kwargs else None
self.flags = [] if flags is None else list(flags)
