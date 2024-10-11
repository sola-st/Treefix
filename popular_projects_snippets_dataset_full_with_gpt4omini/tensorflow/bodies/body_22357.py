# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
self.model_dir = tempfile.mkdtemp()
self.graph = ops.Graph()
with self.graph.as_default():
    self.scaffold = monitored_session.Scaffold()
    with variable_scope.variable_scope('foo', use_resource=True):
        self.global_step = training_util.get_or_create_global_step()
    self.train_op = training_util._increment_global_step(1)
