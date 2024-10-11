# Extracted from ./data/repos/pandas/pandas/io/html.py
super().__init__(*args, **kwargs)
from bs4 import SoupStrainer

self._strainer = SoupStrainer("table")
