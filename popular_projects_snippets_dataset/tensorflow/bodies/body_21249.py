# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("managed_out_of_range")
with ops.Graph().as_default():
    my_op = constant_op.constant(1.0)
    sv = supervisor.Supervisor(logdir=logdir)
    last_step = None
    with sv.managed_session("") as sess:
        for step in range(10):
            last_step = step
            if step == 3:
                raise errors_impl.OutOfRangeError(my_op.op.node_def, my_op.op,
                                                  "all done")
            else:
                self.evaluate(my_op)
      # Supervisor has been stopped.  OutOfRangeError was not thrown.
    self.assertTrue(sv.should_stop())
    self.assertEqual(3, last_step)
