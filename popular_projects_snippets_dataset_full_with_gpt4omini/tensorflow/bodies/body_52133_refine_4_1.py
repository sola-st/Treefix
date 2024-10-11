self = type('Mock', (object,), {'assertAllEqual': lambda x, y: None, 'assertEqual': lambda x, y: None, 'assertIsNone': lambda x: None})() # pragma: no cover
vocabulary_size = 10000 # pragma: no cover
embedding_dimension = 300 # pragma: no cover
shape = (vocabulary_size, embedding_dimension) # pragma: no cover
partition_info = None # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
def assert_all_equal(a, b): assert a == b # pragma: no cover
def assert_equal(a, b): assert a == b # pragma: no cover
def assert_is_none(a): assert a is None # pragma: no cover
self = Mock() # pragma: no cover
self.assertAllEqual = assert_all_equal # pragma: no cover
self.assertEqual = assert_equal # pragma: no cover
self.assertIsNone = assert_is_none # pragma: no cover
vocabulary_size = 10000 # pragma: no cover
embedding_dimension = 300 # pragma: no cover
shape = (vocabulary_size, embedding_dimension) # pragma: no cover
partition_info = None # pragma: no cover

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
