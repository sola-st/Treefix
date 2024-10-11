# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=[],
        max_num_elements=max_num_elements)
    c0 = constant_op.constant(1.0)
    tape.watch(c0)
    l = list_ops.tensor_list_push_back(l, c0)
    l = list_ops.tensor_list_push_back(l, constant_op.constant(2.0))
    t = list_ops.tensor_list_gather(l, [1, 0], element_dtype=dtypes.float32)
    self.assertAllEqual(self.evaluate(t), [2.0, 1.0])
    s = (t[0] + t[1]) * (t[0] + t[1])
dt = tape.gradient(s, c0)
self.assertAllEqual(self.evaluate(dt), 6.0)
