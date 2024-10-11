self = type('Mock', (object,), {'encoding': None, 'fields_to_export': None, 'export_empty_fields': False, 'indent': None})() # pragma: no cover
options = {'encoding': 'utf-8', 'fields_to_export': ['field1', 'field2'], 'export_empty_fields': True, 'indent': 4} # pragma: no cover
dont_fail = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
"""Configure the exporter by popping options from the ``options`` dict.
        If dont_fail is set, it won't raise an exception on unexpected options
        (useful for using with keyword arguments in subclasses ``__init__`` methods)
        """
self.encoding = options.pop('encoding', None)
_l_(21432)
self.fields_to_export = options.pop('fields_to_export', None)
_l_(21433)
self.export_empty_fields = options.pop('export_empty_fields', False)
_l_(21434)
self.indent = options.pop('indent', None)
_l_(21435)
if not dont_fail and options:
    _l_(21437)

    raise TypeError(f"Unexpected options: {', '.join(options.keys())}")
    _l_(21436)
