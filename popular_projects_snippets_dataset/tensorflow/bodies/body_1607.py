# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)
        with ops.control_dependencies([ta.close()]):
            exit(1.0)

    self.evaluate(xla.compile(fn)[0])
