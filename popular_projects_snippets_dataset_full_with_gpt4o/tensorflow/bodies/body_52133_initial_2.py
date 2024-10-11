import numpy as np # pragma: no cover

self = type('MockSelf', (object,), {'assertAllEqual': lambda self, x, y: None, 'assertEqual': lambda self, x, y: None, 'assertIsNone': lambda self, x: None})() # pragma: no cover
vocabulary_size = 1000 # pragma: no cover
embedding_dimension = 300 # pragma: no cover
shape = (vocabulary_size, embedding_dimension) # pragma: no cover
partition_info = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
from l3.Runtime import _l_
self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
_l_(20415)
self.assertEqual(dtypes.float32, dtype)
_l_(20416)
self.assertIsNone(partition_info)
_l_(20417)
aux = embedding_values
_l_(20418)
exit(aux)
