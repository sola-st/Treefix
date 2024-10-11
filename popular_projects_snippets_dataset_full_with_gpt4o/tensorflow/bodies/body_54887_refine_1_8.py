self = type("Mock", (object,), { "assertEqual": lambda x, y: None })() # pragma: no cover

self = type('Mock', (object,), {'assertEqual': lambda self, x, y: x == y})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
from l3.Runtime import _l_
s1 = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(None),
    tensor_shape.Dimension(7)
])
_l_(16697)
s2 = tensor_shape.TensorShape([
    tensor_shape.Dimension(None),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])
_l_(16698)
self.assertEqual([3, 4, 7], s1.merge_with(s2).as_list())
_l_(16699)
