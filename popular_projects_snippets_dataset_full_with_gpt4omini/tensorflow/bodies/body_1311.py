# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(0.0)

    @function.defun_with_attributes(attributes={'_noinline': True})
    def g(x):
        v.assign(x)

    @function.defun_with_attributes(attributes={'_noinline': True})
    def f():
        g(1.0)
        g(2.0)
        g(3.0)
        g(4.0)
        g(5.0)

    f()
    self.assertEqual(5.0, v.read_value().numpy())
