# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
y = np.random.randint(0, 2, 6).astype(np.bool_).reshape(3, 2, 1)  # pylint: disable=too-many-function-args
for f in [math_ops.logical_and, math_ops.logical_or, math_ops.logical_xor]:
    with self.subTest(f=f):
        with self.assertRaisesWithPredicateMatch(
            ValueError, lambda e: "Dimensions must" in str(e)):
            f(x, y)
