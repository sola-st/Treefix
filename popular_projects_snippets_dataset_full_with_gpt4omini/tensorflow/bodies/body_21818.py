# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    p = array_ops.placeholder(dtypes.float32, shape=(3,))
    v = variables.VariableV1(p, name="v",
                             collections=[ops.GraphKeys.LOCAL_VARIABLES])
    sm = session_manager.SessionManager(
        local_init_op=v.initializer,
        local_init_feed_dict={p: [1.0, 2.0, 3.0]},
        ready_op=variables.report_uninitialized_variables())
    sess = sm.prepare_session("")
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
