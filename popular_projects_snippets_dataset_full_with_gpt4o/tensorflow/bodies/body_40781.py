# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    m1 = math_ops.matmul(a, b, transpose_a=transpose_a)
with ops.device('/device:GPU:0'):
    m2 = math_ops.matmul(a, b, transpose_a=transpose_a)
exit((m1, m2))
