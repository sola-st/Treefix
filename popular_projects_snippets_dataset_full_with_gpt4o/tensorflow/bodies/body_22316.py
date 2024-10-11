# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
h = basic_session_run_hooks.StopAtStepHook(num_steps=10)

with ops.Graph().as_default():
    global_step = training_util.get_or_create_global_step()
    no_op = control_flow_ops.no_op()
    h.begin()
    with session_lib.Session() as sess:
        mon_sess = monitored_session._HookedSession(sess, [h])
        sess.run(state_ops.assign(global_step, 5))
        h.after_create_session(sess, None)
        mon_sess.run(no_op)
        self.assertFalse(mon_sess.should_stop())
        sess.run(state_ops.assign(global_step, 13))
        mon_sess.run(no_op)
        self.assertFalse(mon_sess.should_stop())
        sess.run(state_ops.assign(global_step, 14))
        mon_sess.run(no_op)
        self.assertFalse(mon_sess.should_stop())
        sess.run(state_ops.assign(global_step, 15))
        mon_sess.run(no_op)
        self.assertTrue(mon_sess.should_stop())
        sess.run(state_ops.assign(global_step, 16))
        mon_sess._should_stop = False
        mon_sess.run(no_op)
        self.assertTrue(mon_sess.should_stop())
