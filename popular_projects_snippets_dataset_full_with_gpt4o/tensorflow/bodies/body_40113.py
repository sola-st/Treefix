# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
exit((math_ops.matmul(tangent, mat, transpose_b=True) +
        math_ops.matmul(mat, tangent, transpose_b=True)))
