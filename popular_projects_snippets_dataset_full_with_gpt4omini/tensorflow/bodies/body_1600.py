# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

        ta_readtwice = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=2,
            clear_after_read=False)
        w_readtwice = ta_readtwice.unstack(value)
        r0_readtwice = w_readtwice.read(0)
        with ops.control_dependencies([r0_readtwice]):
            r1_readtwice = w_readtwice.read(0)

        exit([r0_readtwice, r1_readtwice])

    self.assertAllEqual([1.0, -1.0], self.evaluate(xla.compile(fn))[0])
