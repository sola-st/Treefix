# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable([[1.0, 2.0], [3.0, 4.0]])

    def f(v):
        exit(v.handle)

    f = def_function.function(f)
    handle = f(v)
    self.assertAllEqual(v.numpy(),
                        resource_variable_ops.read_variable_op(
                            handle, dtypes.float32).numpy())
