import json # pragma: no cover

class MockSerializer: # pragma: no cover
    def serialize(self, obj, **kwargs): # pragma: no cover
        raise NotImplementedError # pragma: no cover
 # pragma: no cover
mock_serializer = MockSerializer() # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
try: # pragma: no cover
    mock_serializer.serialize(obj, **kwargs) # pragma: no cover
except NotImplementedError as e: # pragma: no cover
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
