from typing import Tuple # pragma: no cover

self = type('Mock', (object,), {'item_classes': (dict, tuple)})() # pragma: no cover
item = {} # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self, item_classes):# pragma: no cover
        self.item_classes = item_classes# pragma: no cover
self = Mock(item_classes=(dict,)) # pragma: no cover
item = {} # pragma: no cover

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
    _l_(15953)

    aux = isinstance(item, self.item_classes)
    _l_(15952)
    exit(aux)
aux = True  # accept all items by default
_l_(15954)  # accept all items by default
exit(aux)  # accept all items by default
