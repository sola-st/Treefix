import unittest # pragma: no cover

constant_op = type('MockConstantOp', (object,), {'constant': staticmethod(lambda x, dtype=None: x)})() # pragma: no cover
dtypes = type('MockDtypes', (object,), {'int64': 'int64', 'string': 'string'})() # pragma: no cover
RaggedTensor = type('MockRaggedTensor', (object,), {'from_row_starts': staticmethod(lambda values, row_starts, validate: {'values': values, 'row_starts': row_starts, 'nrows': len(row_starts), 'ragged_rank': 1})})() # pragma: no cover
class MockSelf:  # Mock class to replace `self`# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        assert a == b, f'Assertion failed: {a} != {b}'# pragma: no cover
    def assertIs(self, a, b):# pragma: no cover
        assert a is b, f'Assertion failed: {a} is not {b}'# pragma: no cover
    def assertAllEqual(self, a, b):# pragma: no cover
        assert a == b, f'Assertion failed: {a} != {b}'# pragma: no cover
self = MockSelf() # pragma: no cover

class MockRaggedTensor:# pragma: no cover
    def __init__(self, values, row_starts):# pragma: no cover
        self.values = values# pragma: no cover
        self.row_starts = row_starts# pragma: no cover
        self.nrows = len(row_starts) - 1# pragma: no cover
        self.ragged_rank = 1# pragma: no cover
        self.dtype = dtypes.string# pragma: no cover
    @classmethod# pragma: no cover
    def from_row_starts(cls, values, row_starts, validate=False):# pragma: no cover
        return cls(values, row_starts) # pragma: no cover
RaggedTensor = MockRaggedTensor # pragma: no cover
class MockSelf:# pragma: no cover
    def assertEqual(self, a, b): assert a == b, f'Assertion failed: {a} != {b}'# pragma: no cover
    def assertIs(self, a, b): assert a is b, f'Assertion failed: {a} is not {b}'# pragma: no cover
    def assertAllEqual(self, a, b): assert (a == b).all(), f'Assertion failed: {a} != {b}'# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
from l3.Runtime import _l_
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
_l_(9627)
row_starts = constant_op.constant([0, 2, 2, 5, 6], dtypes.int64)
_l_(9628)

rt = RaggedTensor.from_row_starts(values, row_starts, validate=False)
_l_(9629)
self.assertEqual(rt.dtype, dtypes.string)
_l_(9630)
self.assertEqual(rt.shape.as_list(), [5, None])
_l_(9631)
self.assertEqual(rt.ragged_rank, 1)
_l_(9632)

rt_values = rt.values
_l_(9633)
rt_row_starts = rt.row_starts()
_l_(9634)
rt_nrows = rt.nrows()
_l_(9635)

self.assertIs(rt_values, values)
_l_(9636)
self.assertAllEqual(rt_nrows, 5)
_l_(9637)
self.assertAllEqual(rt_row_starts, row_starts)
_l_(9638)
self.assertAllEqual(rt,
                    [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
_l_(9639)
