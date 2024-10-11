from typing import Dict, Any # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.fields_to_export = None # pragma: no cover
self.export_empty_fields = False # pragma: no cover
self.indent = None # pragma: no cover
options = {'encoding': 'utf-8', 'fields_to_export': ['name', 'age'], 'export_empty_fields': True, 'indent': 4} # pragma: no cover
dont_fail = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
"""Configure the exporter by popping options from the ``options`` dict.
        If dont_fail is set, it won't raise an exception on unexpected options
        (useful for using with keyword arguments in subclasses ``__init__`` methods)
        """
self.encoding = options.pop('encoding', None)
_l_(10038)
self.fields_to_export = options.pop('fields_to_export', None)
_l_(10039)
self.export_empty_fields = options.pop('export_empty_fields', False)
_l_(10040)
self.indent = options.pop('indent', None)
_l_(10041)
if not dont_fail and options:
    _l_(10043)

    raise TypeError(f"Unexpected options: {', '.join(options.keys())}")
    _l_(10042)
