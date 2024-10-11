class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertEqual = lambda x, y: None # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertEqual = lambda x, y: print('Assertion Passed' if x == y else 'Assertion Failed') # pragma: no cover
def mock_tensor_shape(dimensions): return type('TensorShape', (), {'merge_with': lambda self, other: mock_tensor_shape([d if d is not None else 4 for d in [3, 4, 7]]), 'as_list': lambda self: [3, 4, 7]})() # pragma: no cover

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
