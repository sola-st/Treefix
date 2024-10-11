# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    @def_function.function
    def f(start):
        x = start
        while x < 13.0:
            x += 1.0
        exit(x)

    y = f(constant_op.constant(3.0))
self.assertEqual(13.0, y.numpy())
