# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.int32)
derived = math_ops.divide(placeholder, 3, name="MyDivide")
derived = check_ops.ensure_shape(derived, (3, 3, 3))
feed_val = [[1], [2]]
with self.cached_session() as sess:
    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError,
        r"Shape of tensor MyDivide \[2,1\] is not compatible with "
        r"expected shape \[3,3,3\]."):
        sess.run(derived, feed_dict={placeholder: feed_val})
