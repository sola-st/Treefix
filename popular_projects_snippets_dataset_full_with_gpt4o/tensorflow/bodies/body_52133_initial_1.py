import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertAllEqual = lambda a, b: None # pragma: no cover
self.assertEqual = lambda a, b: None # pragma: no cover
self.assertIsNone = lambda a: None # pragma: no cover
vocabulary_size = 10000 # pragma: no cover
embedding_dimension = 300 # pragma: no cover
shape = (10000, 300) # pragma: no cover
dtypes = Mock() # pragma: no cover
partition_info = None # pragma: no cover
embedding_values = np.random.rand(10000, 300).astype(np.float32) # pragma: no cover

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
