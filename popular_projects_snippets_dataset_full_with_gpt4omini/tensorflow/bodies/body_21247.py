# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("managed_session")
with ops.Graph().as_default():
    my_op = constant_op.constant(1.0)
    sv = supervisor.Supervisor(logdir=logdir)
    with sv.managed_session(""):
        for _ in range(10):
            self.evaluate(my_op)
      # Supervisor has been stopped.
    self.assertTrue(sv.should_stop())
