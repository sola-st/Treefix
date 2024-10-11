# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
super(ProfilerHookTest, self).setUp()
self.output_dir = tempfile.mkdtemp()
self.graph = ops.Graph()
self.filepattern = os.path.join(self.output_dir, 'timeline-*.json')
with self.graph.as_default():
    self.global_step = training_util.get_or_create_global_step()
    self.train_op = state_ops.assign_add(self.global_step, 1)
