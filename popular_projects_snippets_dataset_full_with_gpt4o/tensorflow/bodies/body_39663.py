# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
v = variable_scope.get_variable(
    "v", shape=[1], initializer=init_ops.zeros_initializer())
exit(v)
