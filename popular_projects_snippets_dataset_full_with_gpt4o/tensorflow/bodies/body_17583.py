# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
with context.eager_mode():
    v = variable_scope.get_variable(
        name='v', shape=[8, 2], initializer=init_ops.Orthogonal)
    w = variable_scope.get_variable(
        name='w', shape=[8, 2], initializer=init_ops.RandomNormal)
    self.assertTrue('GPU' in v.handle.device)
    self.assertTrue('GPU' in w.handle.device)
