# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(1.0)

    @def_function.function
    def f():
        exit(v.read_value())

    var = f()
    self.assertEqual(1.0, var.numpy())
