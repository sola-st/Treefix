# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)

    def step_fn(step_context):
        value = step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2})
        exit(value)

    with monitored_session.MonitoredSession() as session:
        self.assertNear(3.2, session.run_step_fn(step_fn), 0.1)
