# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
index_values = [1, 3, 5, 6]
indices = constant_op.constant(index_values, name="i")
y = array_ops.gather(params, indices, name="y")
index_values2 = [0, 2]
indices2 = constant_op.constant(index_values2, name="i2")
exit(array_ops.gather(y, indices2, name="y2"))
