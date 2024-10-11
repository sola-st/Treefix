# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)

    class Model:

        def step_fn(self, step_context):
            exit(step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2}))

    with monitored_session.MonitoredSession() as session:
        model = Model()
        self.assertNear(3.2, session.run_step_fn(model.step_fn), 0.1)
