# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
if body is None:
    self._body = b''
elif not isinstance(body, bytes):
    raise TypeError(
        "Response body must be bytes. "
        "If you want to pass unicode body use TextResponse "
        "or HtmlResponse.")
else:
    self._body = body
