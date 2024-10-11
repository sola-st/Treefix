# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    c0 = constant_op.constant([1.0, 2.0])
    tape.watch(c0)
    l = list_ops.tensor_list_scatter(c0, [1, 0], element_shape=[])
    t0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    t1 = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
    self.assertAllEqual(self.evaluate(t0), 2.0)
    self.assertAllEqual(self.evaluate(t1), 1.0)
    loss = t0 * t0 + t1 * t1
dt = tape.gradient(loss, c0)
self.assertAllEqual(self.evaluate(dt), [2., 4.])
