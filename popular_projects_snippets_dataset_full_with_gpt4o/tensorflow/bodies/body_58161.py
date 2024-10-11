# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
with ops.Graph().as_default():
    tensor = array_ops.placeholder(dtype=dtypes.float32, shape=[None, 3, 5])
self.assertAllEqual([None, 3, 5], tensor.shape)

util.set_tensor_shapes([tensor], {"Placeholder": [5, 3, 5]})
self.assertAllEqual([5, 3, 5], tensor.shape)
