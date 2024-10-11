# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
self.model_dir = tempfile.mkdtemp()
self.graph = ops.Graph()
self.steps_per_run = 5
with self.graph.as_default():
    self.scaffold = monitored_session.Scaffold()
    self.global_step = training_util.get_or_create_global_step()
    self.train_op = training_util._increment_global_step(self.steps_per_run)
