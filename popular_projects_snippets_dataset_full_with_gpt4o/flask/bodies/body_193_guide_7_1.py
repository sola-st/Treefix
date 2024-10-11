type('Mock', (object,), {'serialize_data_as_json': lambda self, obj, **kwargs: (_ for _ in ()).throw(NotImplementedError())}) # pragma: no cover
obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
try: # pragma: no cover
    pass
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
