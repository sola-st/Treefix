import numpy as np # pragma: no cover

self = type('Mock', (object,), {'assertAllEqual': lambda self, x, y: x == y, 'assertEqual': lambda self, x, y: x == y, 'assertIsNone': lambda self, x: x is None})() # pragma: no cover
vocabulary_size = 5000 # pragma: no cover
embedding_dimension = 300 # pragma: no cover
shape = (5000, 300) # pragma: no cover
partition_info = None # pragma: no cover
embedding_values = np.random.rand(embedding_dimension) # pragma: no cover

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
