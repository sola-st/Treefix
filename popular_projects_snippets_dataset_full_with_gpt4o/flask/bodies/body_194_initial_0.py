import json # pragma: no cover
from io import StringIO # pragma: no cover

fp = StringIO() # pragma: no cover
self = type('Mock', (object,), {'dumps': lambda s, obj, **kwargs: json.dumps(obj, **kwargs)})() # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON and write to a file.

        :param obj: The data to serialize.
        :param fp: A file opened for writing text. Should use the UTF-8
            encoding to be valid JSON.
        :param kwargs: May be passed to the underlying JSON library.
        """
fp.write(self.dumps(obj, **kwargs))
_l_(22484)
