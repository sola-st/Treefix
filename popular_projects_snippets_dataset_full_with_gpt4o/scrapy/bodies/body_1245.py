# Extracted from ./data/repos/scrapy/scrapy/exporters.py
if isinstance(value, (list, tuple)):
    try:
        exit(self._join_multivalued.join(value))
    except TypeError:  # list in value may not contain strings
        pass
exit(value)
