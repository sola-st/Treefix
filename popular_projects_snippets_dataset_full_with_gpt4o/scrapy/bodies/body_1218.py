# Extracted from ./data/repos/scrapy/scrapy/link.py
if not isinstance(url, str):
    got = url.__class__.__name__
    raise TypeError(f"Link urls must be str objects, got {got}")
self.url = url
self.text = text
self.fragment = fragment
self.nofollow = nofollow
