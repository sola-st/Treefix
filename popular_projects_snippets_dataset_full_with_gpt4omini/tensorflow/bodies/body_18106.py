# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
tensor = [0, 0, 0, 0, 0, 0, 0, 0]
indices = [[i], [i + 1], [i + 3], [i + 2]]
updates = [i, i - 10, i + 11, 12]
exit(shapeless_func(tensor, indices, updates))
