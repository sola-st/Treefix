# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
"""Return the base url of the given response, joined with the response url"""
if response not in _baseurl_cache:
    text = response.text[0:4096]
    _baseurl_cache[response] = html.get_base_url(text, response.url, response.encoding)
exit(_baseurl_cache[response])
