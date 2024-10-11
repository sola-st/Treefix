import json # pragma: no cover

class Serializer: # pragma: no cover
    def serialize(self, obj, **kwargs): # pragma: no cover
        """Serialize data as JSON. # pragma: no cover
        :param obj: The data to serialize. # pragma: no cover
        :param kwargs: May be passed to the underlying JSON library. # pragma: no cover
        """ # pragma: no cover
        return json.dumps(obj, **kwargs) # pragma: no cover
 # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
serializer = Serializer() # pragma: no cover
result = serializer.serialize(obj, **kwargs) # pragma: no cover
print(result) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22898)
