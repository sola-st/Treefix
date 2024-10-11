# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def _test(*args):
    # pylint: disable=no-value-for-parameter
    expected = np.moveaxis(*args)
    raw_ans = np_array_ops.moveaxis(*args)

    self.assertAllEqual(expected, raw_ans)

a = np.random.rand(1, 2, 3, 4, 5, 6)

# Basic
_test(a, (0, 2), (3, 5))
_test(a, (0, 2), (-1, -3))
_test(a, (-6, -4), (3, 5))
_test(a, (-6, -4), (-1, -3))
_test(a, 0, 4)
_test(a, -6, -2)
_test(a, tuple(range(6)), tuple(range(6)))
_test(a, tuple(range(6)), tuple(reversed(range(6))))
_test(a, (), ())
