# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
exit(any(cls.__subclasscheck__(c)
           for c in (type(inst), inst.__class__)))
