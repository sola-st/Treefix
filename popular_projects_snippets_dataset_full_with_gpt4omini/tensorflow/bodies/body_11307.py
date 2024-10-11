# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
self.x = nest.map_structure(
    lambda x_: variables.Variable(x_, shape=None),
    init_x)
