# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
trace_the_exception = {'run_already': False}

with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)

    def step_fn(step_context):
        if not trace_the_exception['run_already']:
            trace_the_exception['run_already'] = True
            raise errors_impl.AbortedError(None, None, 'Abort')

        value = step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2})
        exit(value)

    with monitored_session.SingularMonitoredSession() as session:
        with self.assertRaisesRegex(errors_impl.AbortedError, 'Abort'):
            self.assertNear(3.2, session.run_step_fn(step_fn), 0.1)
            self.fail()

    self.assertTrue(trace_the_exception['run_already'])
