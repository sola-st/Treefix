class TestTensorShape: # Mock test class # pragma: no cover
    def assertEqual(self, a, b): pass # Mock assertEqual method # pragma: no cover
test = TestTensorShape() # Create an instance of the mock test class # pragma: no cover

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
