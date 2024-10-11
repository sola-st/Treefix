import json # pragma: no cover

class JSONSerializer: # pragma: no cover
    def serialize(self, obj, **kwargs): # pragma: no cover
        try: # pragma: no cover
            return json.dumps(obj, **kwargs) # pragma: no cover
        except Exception as e: # pragma: no cover
            print(f'Error serializing object: {e}') # pragma: no cover
serializer = JSONSerializer() # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
serializer.serialize(obj, **kwargs) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22898)
