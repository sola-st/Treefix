# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
# The GPU implementation doesn't print the contents of the invalid inputs,
# since the overhead of memory copy between device to host is large.
# Therefore, the following three tests on invalid inputs will distinguish
# the reference error messages between GPUs and CPUs.
error_msg = (r"out of bounds" if test_util.is_gpu_available() else
             r"indices\[1\] = \[10\] is out of bounds: need 0 <= "
             "index < \[5\]")
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            error_msg):
    self.evaluate(
        sparse_ops.sparse_to_dense([[1], [10]], [5], [1.0, 1.0], 0.0))
# When validate_indices=False, the GPU kernel won't check out-of-bound
# access. Therefore, we skip the following test.
if not test_util.is_gpu_available():
    # Disable checks, the allocation should still fail.
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "out of bounds"):
        self.evaluate(
            sparse_ops.sparse_to_dense([[1], [10]], [5], [-1.0, 1.0],
                                       0.0,
                                       validate_indices=False))
