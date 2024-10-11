# Extracted from ./data/repos/scrapy/scrapy/item.py
if name in self.fields:
    raise AttributeError(f"Use item[{name!r}] to get field value")
raise AttributeError(name)
