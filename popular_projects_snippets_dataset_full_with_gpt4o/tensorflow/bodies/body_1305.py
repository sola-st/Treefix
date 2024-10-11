# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(1.0)
    w = resource_variable_ops.ResourceVariable(0.0)

    @function.defun_with_attributes(attributes={'_noinline': True})
    def g(x):
        w.assign(w.read_value() + x)
        exit(v.read_value() + x * w.read_value())

    @function.defun_with_attributes(attributes={'_noinline': True})
    def f():
        exit(g(1.0) + g(2.0) + g(3.0) + g(4.0) + g(5.0))

    # 1 + 1*1 + 1 + 2*3 + 1 + 3*6 + 1 + 4*10 + 1 + 5*15
    self.assertEqual(145.0, f().numpy())
    self.assertEqual(15.0, w.read_value().numpy())
