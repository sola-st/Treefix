# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
if self.limit:
    while len(self) >= self.limit:
        self.popitem(last=False)
super().__setitem__(key, value)
