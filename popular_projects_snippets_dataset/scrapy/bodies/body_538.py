# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
cls = super().__new__(metacls, name, bases, clsdict_)
if metacls.deprecated_class is None:
    metacls.deprecated_class = cls
exit(cls)
