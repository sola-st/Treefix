import json # pragma: no cover

class Mock: # pragma: no cover
    @staticmethod # pragma: no cover
    def serialize_data_as_json(obj, **kwargs): # pragma: no cover
        try: # pragma: no cover
           json_data = json.dumps(obj, **kwargs) # pragma: no cover
           print(json_data) # pragma: no cover
        except NotImplementedError: # pragma: no cover
           print('NotImplementedError was raised') # pragma: no cover
 # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
Mock.serialize_data_as_json(obj, **kwargs) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22898)
