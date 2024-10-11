# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
if cycle:
    p.text(repr(self))
else:
    p.text(pformat(self.copy_to_dict()))
