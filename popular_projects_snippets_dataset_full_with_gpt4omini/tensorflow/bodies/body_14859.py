# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError, r''):
    np_math_ops.average(np.ones([2, 3]), weights=np.ones([2, 4]))
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError, r''):
    np_math_ops.average(np.ones([2, 3]), axis=0, weights=np.ones([2, 4]))
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError, r''):
    np_math_ops.average(np.ones([2, 3]), axis=0, weights=np.ones([]))
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError, r''):
    np_math_ops.average(np.ones([2, 3]), axis=0, weights=np.ones([5]))
