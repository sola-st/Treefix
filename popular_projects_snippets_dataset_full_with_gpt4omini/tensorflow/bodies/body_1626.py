# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=0, infer_shape=True)
        size = ta.size()
        ta = ta.unstack(array_ops.zeros([0, 3, 5]))
        exit([size, ta.stack()])

    [size, stack] = self.evaluate(xla.compile(fn))
    self.assertEqual(0, size)
    self.assertAllEqual([0, 3, 5], stack.shape)
    # Concatenating zero tensors along their first dimension gives a
    # first dimension of zero
    if not control_flow_util.ENABLE_CONTROL_FLOW_V2:

        def fn():
            ta = tensor_array_ops.TensorArray(
                dtype=dtypes.float32, size=0, infer_shape=True)
            ta = ta.unstack(array_ops.zeros([0, 3, 5]))
            exit(ta.concat())

        # TODO(b/122315751): Enable this.
        self.assertAllEqual([0, 5], self.evaluate(xla.compile(fn))[0].shape)
