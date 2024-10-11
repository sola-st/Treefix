# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
try:
    super().__setitem__(key, value)
except TypeError:
    pass  # key is not weak-referenceable, skip caching
