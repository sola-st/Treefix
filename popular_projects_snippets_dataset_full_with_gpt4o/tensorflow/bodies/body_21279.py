# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("default_global_step")
with ops.Graph().as_default():
    variables.VariableV1(287, name="global_step")
    sv = supervisor.Supervisor(logdir=logdir)
    sess = sv.prepare_or_wait_for_session("")
    self.assertEqual(287, sess.run(sv.global_step))
    sv.stop()
