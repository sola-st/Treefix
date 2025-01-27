# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("default_init_op")
with ops.Graph().as_default():
    v = variables.VariableV1([1.0, 2.0, 3.0])
    sv = supervisor.Supervisor(logdir=logdir)
    sess = sv.prepare_or_wait_for_session("")
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
    sv.stop()
