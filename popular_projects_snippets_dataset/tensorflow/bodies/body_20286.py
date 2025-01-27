# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
tmp = array_ops.reshape(arg1, array_ops.shape(arg0))
ret0 = arg0 + tmp
ret1 = math_ops.matmul(arg0, arg1)
ret2 = array_ops.concat([arg0, tmp], 0)
exit((ret0, ret1, ret2))
