# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("feed_dict_init_op")
with ops.Graph().as_default():
    p = array_ops.placeholder(dtypes.float32, shape=(3,))
    v = variables.VariableV1(p, name="v")
    sv = supervisor.Supervisor(
        logdir=logdir,
        init_op=variables.global_variables_initializer(),
        init_feed_dict={p: [1.0, 2.0, 3.0]})
    sess = sv.prepare_or_wait_for_session("")
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
    sv.stop()
