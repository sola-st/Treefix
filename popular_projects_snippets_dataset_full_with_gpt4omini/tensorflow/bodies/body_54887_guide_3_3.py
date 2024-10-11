class MockDimension: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
class MockTensorShape: # pragma: no cover
    def __init__(self, dimensions): # pragma: no cover
        self.dimensions = dimensions # pragma: no cover
    def merge_with(self, other): # pragma: no cover
        return MockTensorShape([self.dimensions[0].value, other.dimensions[1].value, self.dimensions[2].value]) # pragma: no cover
    def as_list(self): # pragma: no cover
        return [dim.value for dim in self.dimensions] # pragma: no cover
self = type('MockTestCase', (object,), {'assertEqual': lambda self, a, b: print('Test passed' if a == b else 'Test failed')})() # pragma: no cover

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
