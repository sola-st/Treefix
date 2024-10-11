# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
from l3.Runtime import _l_
for dtype in self.numeric_types - {np.uint8, np.int8}:
    _l_(17134)

    self._assertOpOutputMatchesExpected(
        xla.neg,
        args=(np.array([1, 2, 3], dtype=dtype),),
        expected=np.array([-1, -2, -3], dtype=dtype))
    _l_(17133)
