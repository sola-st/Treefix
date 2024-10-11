# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(10.0)

    @function.defun_with_attributes(attributes={'_noinline': True})
    def g():
        exit(v.read_value())

    @function.defun_with_attributes(attributes={'_noinline': True})
    def f():
        exit(g() + g() + g() + g() + g())

    self.assertEqual(50.0, f().numpy())
