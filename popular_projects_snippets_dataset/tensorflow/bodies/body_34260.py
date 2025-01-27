# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    c = constant_op.constant([1.0, 2.0])
    tape.watch(c)
    l = list_ops.tensor_list_from_tensor(c, element_shape=[])
    c2 = constant_op.constant(3.0)
    tape.watch(c2)
    l = list_ops.tensor_list_set_item(l, 0, c2)
    e = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    ee = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
    y = e * e + ee * ee
grad_c, grad_c2 = tape.gradient(y, [c, c2])
self.assertAllEqual(self.evaluate(grad_c), [0.0, 4.0])
self.assertAllEqual(self.evaluate(grad_c2), 6.0)
