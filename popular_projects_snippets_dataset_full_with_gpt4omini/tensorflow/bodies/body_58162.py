# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
with ops.Graph().as_default():
    tensor = array_ops.placeholder(dtype=dtypes.float32)

util.set_tensor_shapes([tensor], {"Placeholder": [1, 3, 5]})
self.assertAllEqual([1, 3, 5], tensor.shape)
