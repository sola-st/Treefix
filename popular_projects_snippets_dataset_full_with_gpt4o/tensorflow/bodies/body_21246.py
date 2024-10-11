# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("basics")
with ops.Graph().as_default():
    my_op = constant_op.constant(1.0)
    sv = supervisor.Supervisor(logdir=logdir)
    sess = sv.prepare_or_wait_for_session("")
    for _ in range(10):
        self.evaluate(my_op)
    sess.close()
    sv.stop()
