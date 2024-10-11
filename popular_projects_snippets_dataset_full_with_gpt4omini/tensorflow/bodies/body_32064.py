# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
self.assertAllEqual(
    np.array(truth).astype("U"), np.array(actual).astype("U"))
