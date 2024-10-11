# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
v = variable_scope.get_variable(
    "v", shape=[1], initializer=init_ops.zeros_initializer(),
    use_resource=True)
v2 = variable_scope.get_variable(
    "v2", shape=[1], initializer=init_ops.zeros_initializer(),
    use_resource=True)
manual = _ManualScope()
exit((v, v + 1., v2, manual, manual()))
