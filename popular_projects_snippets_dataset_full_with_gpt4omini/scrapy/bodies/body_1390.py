# Extracted from ./data/repos/scrapy/scrapy/item.py
if key in self.fields:
    self._values[key] = value
else:
    raise KeyError(f"{self.__class__.__name__} does not support field: {key}")
