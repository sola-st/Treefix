# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
exit(lambda x, un_op: ar.build_recursive_hd_all_reduce(
    x, math_ops.add, un_op))
