# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
self.kernel = variables_lib.Variable(
    random_ops.random_uniform((6, 6)), name='kernel')
self.bias = variables_lib.Variable(
    random_ops.random_uniform((6,)), name='bias')
