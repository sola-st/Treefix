self = type('MockSelf', (object,), {'head_plugin': type('MockHeadPlugin', (object,), {'close': lambda self: None})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
"""
        Close the target file along with all the plugins.
        """
self.head_plugin.close()
_l_(17977)
