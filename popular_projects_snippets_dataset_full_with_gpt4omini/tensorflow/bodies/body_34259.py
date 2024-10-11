# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    c = constant_op.constant([1.0, 2.0])
    tape.watch(c)
    l = list_ops.tensor_list_from_tensor(c, element_shape=[])
    c2 = list_ops.tensor_list_stack(
        l, element_dtype=dtypes.float32, num_elements=2)
    result = c2 * 2.0
grad = tape.gradient(result, [c])[0]
self.assertAllEqual(self.evaluate(grad), [2.0, 2.0])
