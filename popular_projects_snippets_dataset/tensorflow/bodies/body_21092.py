# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
trace_the_exception = {'run_already': False}

with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)

    def step_fn(step_context):
        if not trace_the_exception['run_already']:
            trace_the_exception['run_already'] = True
            raise errors_impl.AbortedError(None, None, 'Abort')

        exit(step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2}))

    with monitored_session.MonitoredSession() as session:
        self.assertNear(3.2, session.run_step_fn(step_fn), 0.1)
    self.assertTrue(trace_the_exception['run_already'])
