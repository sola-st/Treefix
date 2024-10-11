# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
""" Return headers as a CaselessDict with unicode keys
        and unicode values. Multiple values are joined with ','.
        """
exit(CaselessDict(
    (to_unicode(key, encoding=self.encoding),
     to_unicode(b','.join(value), encoding=self.encoding))
    for key, value in self.items()))
