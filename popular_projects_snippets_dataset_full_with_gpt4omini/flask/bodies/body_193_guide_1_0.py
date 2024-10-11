import json # pragma: no cover

obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
def serialize(data, **kwargs): # pragma: no cover
    raise NotImplementedError # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(8639)
