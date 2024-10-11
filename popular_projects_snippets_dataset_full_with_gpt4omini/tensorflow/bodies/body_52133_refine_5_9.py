import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
vocabulary_size = 10000 # pragma: no cover
embedding_dimension = 128 # pragma: no cover
shape = (vocabulary_size, embedding_dimension) # pragma: no cover
partition_info = None # pragma: no cover
embedding_values = np.random.rand(vocabulary_size, embedding_dimension).astype(np.float32) # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda self, x, y: print(f'Asserting equality: {x} == {y}'), 'assertEqual': lambda self, x, y: print(f'Asserting equal: {x} == {y}'), 'assertIsNone': lambda self, x: print(f'Asserting is None: {x} is None')})() # pragma: no cover
vocabulary_size = 10000 # pragma: no cover
embedding_dimension = 128 # pragma: no cover
shape = (vocabulary_size, embedding_dimension) # pragma: no cover
partition_info = None # pragma: no cover
embedding_values = np.random.rand(vocabulary_size, embedding_dimension).astype(np.float32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
from l3.Runtime import _l_
self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
_l_(7366)
self.assertEqual(dtypes.float32, dtype)
_l_(7367)
self.assertIsNone(partition_info)
_l_(7368)
aux = embedding_values
_l_(7369)
exit(aux)
