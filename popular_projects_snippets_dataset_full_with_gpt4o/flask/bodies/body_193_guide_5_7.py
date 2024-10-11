import json # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self, obj): # pragma: no cover
        self.obj = obj # pragma: no cover
    def serialize_data_as_json(self, **kwargs): # pragma: no cover
        """Serialize data as JSON. # pragma: no cover
        :param obj: The data to serialize. # pragma: no cover
        :param kwargs: May be passed to the underlying JSON library. # pragma: no cover
        """ # pragma: no cover
        raise NotImplementedError # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
mock = Mock(obj) # pragma: no cover
try: # pragma: no cover
    mock.serialize_data_as_json(**kwargs) # pragma: no cover
except NotImplementedError: # pragma: no cover
    print('NotImplementedError was raised') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22898)
