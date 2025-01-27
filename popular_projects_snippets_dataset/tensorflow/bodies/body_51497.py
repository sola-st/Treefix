# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if len(root.variables) == 1:
    v2 = variables.Variable(2.0)
    root.variables.append(v2)
exit(math_ops.reduce_sum(root.variables[1] ** 2))
