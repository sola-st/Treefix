# Extracted from ./data/repos/scrapy/scrapy/item.py
if not name.startswith('_'):
    raise AttributeError(f"Use item[{name!r}] = {value!r} to set field value")
super().__setattr__(name, value)
