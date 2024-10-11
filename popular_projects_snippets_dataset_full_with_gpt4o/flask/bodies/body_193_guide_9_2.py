obj = {'key': 'value'} # pragma: no cover
kwargs = {} # pragma: no cover
def mock_serialize_data_as_json(obj, **kwargs): # pragma: no cover
    """Serialize data as JSON. # pragma: no cover
    :param obj: The data to serialize. # pragma: no cover
    :param kwargs: May be passed to the underlying JSON library. # pragma: no cover
    """ # pragma: no cover
    raise NotImplementedError # uncovered # pragma: no cover
try: # pragma: no cover
    mock_serialize_data_as_json(obj, **kwargs) # pragma: no cover
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
