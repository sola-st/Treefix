# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class SummarizedTensor(extension_type.ExtensionType):
    values: ops.Tensor
    mean: ops.Tensor
    max: ops.Tensor

    def __init__(self, values):
        self.values = ops.convert_to_tensor(values)
        self.mean = math_ops.reduce_mean(values)
        self.max = math_ops.reduce_max(values)

x = SummarizedTensor([[1.0, 2, 3], [4, 5, 6]])
self.assertAllEqual(x.values, [[1.0, 2, 3], [4, 5, 6]])
self.assertAllEqual(x.mean, 3.5)
self.assertAllEqual(x.max, 6)
