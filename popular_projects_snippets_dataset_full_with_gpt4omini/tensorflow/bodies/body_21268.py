# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("default_init_op")
with ops.Graph().as_default():
    v = variables.VariableV1([1.0, 2.0, 3.0])

    def _init_fn(sess):
        sess.run(v.initializer)

    sv = supervisor.Supervisor(logdir=logdir, init_op=None, init_fn=_init_fn)
    sess = sv.prepare_or_wait_for_session("")
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
    sv.stop()
