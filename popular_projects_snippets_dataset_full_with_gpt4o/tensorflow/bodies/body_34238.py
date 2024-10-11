# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    t = constant_op.constant(5.)
    tape.watch(t)
    l = list_ops.tensor_list_reserve(
        element_dtype=dtypes.float32, element_shape=[], num_elements=3)
    l = list_ops.tensor_list_set_item(l, 1, 2. * t)
    e = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
    self.assertAllEqual(self.evaluate(e), 10.0)
self.assertAllEqual(self.evaluate(tape.gradient(e, t)), 2.0)
