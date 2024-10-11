from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.head_plugin = MagicMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
"""
        Close the target file along with all the plugins.
        """
self.head_plugin.close()
_l_(7552)
