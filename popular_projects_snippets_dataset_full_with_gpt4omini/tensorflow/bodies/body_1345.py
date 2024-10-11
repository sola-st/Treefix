# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    @def_function.function
    def f(pred, value):
        if pred:
            exit(value + 1.0)
        else:
            exit(value - 1.0)

    plus_one = f(constant_op.constant(True), constant_op.constant(10.0))
    minus_one = f(constant_op.constant(False), constant_op.constant(10.0))
self.assertEqual(11.0, plus_one.numpy())
self.assertEqual(9.0, minus_one.numpy())
