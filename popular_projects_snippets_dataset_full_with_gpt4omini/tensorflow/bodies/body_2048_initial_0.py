import numpy as np # pragma: no cover

class Mock:  # Create a mock class to define the attributes and methods # pragma: no cover
    numeric_types = {np.float16, np.float32, np.float64, np.int16, np.int32, np.int64, np.uint16, np.uint32, np.uint64} # pragma: no cover
    def _assertOpOutputMatchesExpected(self, op, args, expected): # pragma: no cover
        assert np.array_equal(op(*args), expected), 'Output does not match expected value.' # pragma: no cover
self = Mock() # pragma: no cover
xla = type('MockXLA', (), {'neg': lambda x: -x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
from l3.Runtime import _l_
for dtype in self.numeric_types - {np.uint8, np.int8}:
    _l_(5352)

    self._assertOpOutputMatchesExpected(
        xla.neg,
        args=(np.array([1, 2, 3], dtype=dtype),),
        expected=np.array([-1, -2, -3], dtype=dtype))
    _l_(5351)
