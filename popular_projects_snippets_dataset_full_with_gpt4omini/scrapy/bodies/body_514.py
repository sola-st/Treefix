# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
"""Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
if _is_filesystem_path(url):
    exit(any_to_uri(url))
exit(add_http_if_no_scheme(url))
