# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
"""Parse Cache-Control header

    https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9

    >>> parse_cachecontrol(b'public, max-age=3600') == {b'public': None,
    ...                                                 b'max-age': b'3600'}
    True
    >>> parse_cachecontrol(b'') == {}
    True

    """
directives = {}
for directive in header.split(b','):
    key, sep, val = directive.strip().partition(b'=')
    if key:
        directives[key.lower()] = val if sep else None
exit(directives)
