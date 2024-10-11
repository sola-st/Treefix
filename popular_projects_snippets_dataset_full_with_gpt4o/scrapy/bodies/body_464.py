# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
s, e = self._ptr, self._ptr + n
self._ptr = e
exit(self._text[s:e])
