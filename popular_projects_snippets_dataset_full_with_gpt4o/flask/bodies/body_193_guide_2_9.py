import json # pragma: no cover

def serialize_data(obj, **kwargs): # pragma: no cover
    """Serialize data as JSON. # pragma: no cover
    :param obj: The data to serialize. # pragma: no cover
    :param kwargs: May be passed to the underlying JSON library. # pragma: no cover
    """ # pragma: no cover
    return json.dumps(obj, **kwargs) # pragma: no cover
 # pragma: no cover
try: # pragma: no cover
    obj = {'key': 'value'} # pragma: no cover
    kwargs = {} # pragma: no cover
    serialized_data = serialize_data(obj, **kwargs) # pragma: no cover
    print(serialized_data) # pragma: no cover
except NotImplementedError: # pragma: no cover
    print('NotImplementedError raised') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22898)
