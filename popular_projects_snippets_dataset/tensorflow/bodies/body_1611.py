# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=3,
            infer_shape=False)
        w0 = ta.write(0, [[4.0, 5.0]])
        w1 = w0.write(1, [[3.0, 1.0]])
        with ops.control_dependencies([w1.close()]):
            exit(1.0)

    self.evaluate(xla.compile(fn))
