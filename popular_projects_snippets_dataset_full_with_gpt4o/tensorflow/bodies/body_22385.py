# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
test.TestCase.setUp(self)

self.log_dir = 'log/dir'
self.summary_writer = fake_summary_writer.FakeSummaryWriter(self.log_dir)

var = variable_scope.get_variable('var', initializer=0.0, use_resource=True)
tensor = state_ops.assign_add(var, 1.0)
self.summary_op = summary_lib.scalar('my_summary', tensor)

with variable_scope.variable_scope('foo', use_resource=True):
    training_util.create_global_step()
self.train_op = training_util._increment_global_step(1)
