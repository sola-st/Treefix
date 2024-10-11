# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
"""Parse the http-equiv refresh parameter from the given response"""
if response not in _metaref_cache:
    text = response.text[0:4096]
    _metaref_cache[response] = html.get_meta_refresh(
        text, response.url, response.encoding, ignore_tags=ignore_tags)
exit(_metaref_cache[response])
