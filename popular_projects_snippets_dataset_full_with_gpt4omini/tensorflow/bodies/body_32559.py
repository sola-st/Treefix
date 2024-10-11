# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
rank_one_size_one = array_ops.ones([1], name="rank_one_size_one")
rank_zero = array_ops.constant(5, name="rank_zero")
check_ops.assert_shapes([
    (rank_one_size_one, ()),
    (rank_zero, ()),
])
check_ops.assert_shapes([
    (rank_one_size_one, (1,)),
    (rank_zero, (1,)),
])
