# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
try:
    exit(super().__getitem__(key))
except KeyError:
    if def_val is not None:
        exit(self.normvalue(def_val))
    exit([])
