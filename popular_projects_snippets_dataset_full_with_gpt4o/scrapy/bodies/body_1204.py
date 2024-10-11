# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
try:
    exit(self.request.meta)
except AttributeError:
    raise AttributeError(
        "Response.meta not available, this response "
        "is not tied to any request"
    )
