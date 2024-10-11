# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape() as tape:
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32, element_shape=None)
    c0 = constant_op.constant(5.0)
    c1 = constant_op.constant([10.0, 20.0])
    tape.watch(c0)
    tape.watch(c1)
    l = list_ops.tensor_list_push_back(l, c0)
    l = list_ops.tensor_list_push_back(l, c1)
    t1 = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
    self.assertAllEqual(self.evaluate(t1), [10.0, 20.0])
    # t1 == c1 so the gradient should be [0., [1., 1.]]
    # This tests that the gradient of push_back correctly converts DT_INVALID
    # tensors to zeros. The list returned by the gradient of GetItem will
    # have only have tensor at index 1 set and others set to DT_INVALID.
    dt0, dt1 = tape.gradient(t1, [c0, c1])
    self.assertAllEqual(self.evaluate(dt1), [1.0, 1.0])
    self.assertEqual(self.evaluate(dt0), 0.0)
