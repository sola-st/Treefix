# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    x = array_ops.placeholder(dtype=dtypes.float32)
    y = x + 1
    hook = basic_session_run_hooks.FeedFnHook(
        feed_fn=lambda: {x: 1.0})
    hook.begin()
    mon_sess = monitored_session._HookedSession(sess, [hook])
    self.assertEqual(mon_sess.run(y), 2)
