# Extracted from ./data/repos/scrapy/scrapy/http/common.py
def newsetter(self, value):
    c = self.__class__.__name__
    msg = f"{c}.{attrname} is not modifiable, use {c}.replace() instead"
    raise AttributeError(msg)
exit(newsetter)
