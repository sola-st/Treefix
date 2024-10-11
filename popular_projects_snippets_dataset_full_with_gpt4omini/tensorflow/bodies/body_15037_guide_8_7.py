class MockAssertions: # pragma: no cover
    def assertEqual(self, a, b): print(f'AssertEqual: {{a}} == {{b}}') # pragma: no cover
    def assertIs(self, a, b): print(f'AssertIs: {{a}} is {{b}}') # pragma: no cover
    def assertAllEqual(self, a, b): print(f'AssertAllEqual: {{a}} == {{b}}') # pragma: no cover
self = MockAssertions() # pragma: no cover
class MockShape: # pragma: no cover
    @staticmethod # pragma: no cover
    def as_list(): return [5, None] # pragma: no cover
def mocked_getitem(idx): # pragma: no cover
    if idx == 0: return constant_op.constant([b'a', b'b']) # pragma: no cover
    elif idx == 1: return constant_op.constant([]) # pragma: no cover
    elif idx == 2: return constant_op.constant([b'c', b'd', b'e']) # pragma: no cover
    elif idx == 3: return constant_op.constant([b'f']) # pragma: no cover
    elif idx == 4: return constant_op.constant([b'g']) # pragma: no cover

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
