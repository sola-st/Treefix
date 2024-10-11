# Extracted from ./data/repos/scrapy/scrapy/squeues.py
s = super().pop()
if s:
    exit(deserialize(s))
