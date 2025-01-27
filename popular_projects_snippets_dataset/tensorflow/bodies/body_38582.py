# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
ret = np.copy(x)
ret = ret.transpose(perm)
exit(ret)
