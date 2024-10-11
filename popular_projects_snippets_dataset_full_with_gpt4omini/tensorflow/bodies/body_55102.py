# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class AlignedTensors(extension_type.ExtensionType):
    x: ops.Tensor
    y: ops.Tensor

    def __validate__(self):
        self.x.shape.assert_is_compatible_with(self.y.shape)

aligned = AlignedTensors([1, 2, 3], ['a', 'b', 'c'])
self.assertAllEqual(aligned.x, [1, 2, 3])
self.assertAllEqual(aligned.y, [b'a', b'b', b'c'])

with self.assertRaises(ValueError):
    AlignedTensors([1, 2, 3], ['a', 'b', 'c', 'd'])
