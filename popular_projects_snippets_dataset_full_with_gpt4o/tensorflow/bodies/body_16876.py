# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
index_values = [1, 3]
indices = constant_op.constant(index_values, name="i")
exit(array_ops.gather(params, indices, name="y"))
