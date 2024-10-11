import numpy as np # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertAllEqual = lambda a, b: np.testing.assert_array_equal(a, b) # pragma: no cover

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
