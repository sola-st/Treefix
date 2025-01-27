# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("managed_user_error")
with ops.Graph().as_default():
    my_op = constant_op.constant(1.0)
    sv = supervisor.Supervisor(logdir=logdir)
    last_step = None
    with self.assertRaisesRegex(RuntimeError, "failing here"):
        with sv.managed_session("") as sess:
            for step in range(10):
                last_step = step
                if step == 1:
                    raise RuntimeError("failing here")
                else:
                    self.evaluate(my_op)
      # Supervisor has been stopped.
    self.assertTrue(sv.should_stop())
    self.assertEqual(1, last_step)
