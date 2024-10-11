import numpy as np # pragma: no cover

class Mock:# pragma: no cover
    numeric_types = {np.int32, np.int64, np.float32, np.float64}# pragma: no cover
    def _assertOpOutputMatchesExpected(self, op, args, expected):# pragma: no cover
        result = op(*args)# pragma: no cover
        assert np.array_equal(result, expected), f'Expected {expected}, but got {result}'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
class MockXLA:# pragma: no cover
    @staticmethod# pragma: no cover
    def neg(x):# pragma: no cover
        return -x# pragma: no cover
# pragma: no cover
xla = MockXLA() # pragma: no cover

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
