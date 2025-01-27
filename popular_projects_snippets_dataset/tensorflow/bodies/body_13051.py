# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = variable_scope.get_variable("x", shape=[10, 10], dtype=dtypes.float32)
_ = dropout_fn(x, rate=0.1)
