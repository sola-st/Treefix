from typing import List, Type, Any # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'item_classes': (str, int)})() # pragma: no cover
item = 'example' # pragma: no cover

from typing import Type, Tuple # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'item_classes': (str, int)})() # pragma: no cover
item = 'example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
"""
        Return ``True`` if `item` should be exported or ``False`` otherwise.

        :param item: scraped item which user wants to check if is acceptable
        :type item: :ref:`Scrapy items <topics-items>`
        :return: `True` if accepted, `False` otherwise
        :rtype: bool
        """
if self.item_classes:
    _l_(4378)

    aux = isinstance(item, self.item_classes)
    _l_(4377)
    exit(aux)
aux = True  # accept all items by default
_l_(4379)  # accept all items by default
exit(aux)  # accept all items by default
