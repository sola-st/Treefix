# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v0 = resource_variable_ops.ResourceVariable(1.0)

    def f():
        x = v0 * v0
        exit(x)

    grads = backprop.implicit_grad(f)()
self.assertEqual(2., grads[0][0].numpy())
