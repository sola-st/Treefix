# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if not context.executing_eagerly():
    exit()

values = [[1., 2.], [3., 4., 5.], [6.]]
r = ragged_factory_ops.constant(values)
i = 0
for elem in r:
    self.assertAllEqual(elem, values[i])
    i += 1
