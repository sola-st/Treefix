# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
test.TestCase.setUp(self)

self.log_dir = 'log/dir'
self.summary_writer = fake_summary_writer.FakeSummaryWriter(self.log_dir)

var = variables_lib.Variable(0.0)
tensor = state_ops.assign_add(var, 1.0)
tensor2 = tensor * 2
self.summary_op = summary_lib.scalar('my_summary', tensor)
self.summary_op2 = summary_lib.scalar('my_summary2', tensor2)

training_util.get_or_create_global_step()
self.train_op = training_util._increment_global_step(1)
