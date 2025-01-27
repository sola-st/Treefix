# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32, element_shape=[])
    c = constant_op.constant(1.0)
    tape.watch(c)
    l = list_ops.tensor_list_push_back(l, c)
    l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    e = 2 * e
self.assertAllEqual(self.evaluate(tape.gradient(e, [c])[0]), 2.0)
