# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(1.0)

    def f(v):
        v.assign_add(1.0)
        exit(v)

    f = def_function.function(f)

    var = f(v)
    self.assertEqual(2.0, var.numpy())
