# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# The Shape op kernel on GPU places the output in host memory.
value = constant_op.constant([1.]).gpu()
shape = array_ops.shape(value)
self.assertEqual([1], shape.numpy())
