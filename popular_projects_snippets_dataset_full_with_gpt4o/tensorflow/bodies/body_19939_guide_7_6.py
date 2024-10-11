type_name = type('Mock', (object,), { # pragma: no cover
    'get_embedding_variable_name': lambda self: None # pragma: no cover
}) # pragma: no cover
 # pragma: no cover
mock_base = type_name() # pragma: no cover
 # pragma: no cover
try: # pragma: no cover
    mock_base.get_embedding_variable_name() # pragma: no cover
    raise NotImplementedError('not impl') # pragma: no cover
except NotImplementedError as e: # pragma: no cover
    print(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
from l3.Runtime import _l_
"""Returns the embedding variable name.

    Feature key name and embedding variable name are usually one-to-one mapping.
    But for shared embedding columns, it is many-to-one mapping.
    """
raise NotImplementedError('not impl')
_l_(18511)
