class Mock: pass# pragma: no cover
self = Mock()# pragma: no cover
self.assertEqual = lambda x, y: print('Assertion Passed' if x == y else 'Assertion Failed')# pragma: no cover
# pragma: no cover
def mock_tensor_shape(dimensions):# pragma: no cover
    class Dimension:# pragma: no cover
        def __init__(self, value):# pragma: no cover
            self.value = value# pragma: no cover
    class TensorShape:# pragma: no cover
        def __init__(self, dims):# pragma: no cover
            self.dims = dims# pragma: no cover
        def merge_with(self, other):# pragma: no cover
            merged_dims = [max(d.value if d.value is not None else 1, o.value if o.value is not None else 1) for d, o in zip(self.dims, other.dims)]# pragma: no cover
            return TensorShape([Dimension(d) for d in merged_dims])# pragma: no cover
        def as_list(self):# pragma: no cover
            return [d.value for d in self.dims] # pragma: no cover
    return TensorShape([Dimension(d) for d in dimensions])# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
from l3.Runtime import _l_
s1 = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(None),
    tensor_shape.Dimension(7)
])
_l_(5000)
s2 = tensor_shape.TensorShape([
    tensor_shape.Dimension(None),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])
_l_(5001)
self.assertEqual([3, 4, 7], s1.merge_with(s2).as_list())
_l_(5002)
