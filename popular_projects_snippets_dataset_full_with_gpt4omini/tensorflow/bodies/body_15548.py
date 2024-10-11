# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
if callable(a):
    a = a()
if callable(b):
    b = b()
actual = ragged_math_ops.matmul(a, b, **kwargs)
expected = self.eager_ragged_matmul(a, b, **kwargs)
self.assertAllEqual(actual, expected)

if expected_shape is not None and not kwargs:
    if context.executing_eagerly():
        self.assertTrue(actual.shape.is_compatible_with(expected_shape))
    else:
        self.assertEqual(actual.shape.as_list(), expected_shape)
