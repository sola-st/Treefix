# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    trace_the_hook = {'before_run': False, 'after_run': False}

    class Hook(session_run_hook.SessionRunHook):

        def before_run(self, run_context):
            trace_the_hook['before_run'] = True

        def after_run(self, run_context, run_values):
            trace_the_hook['after_run'] = True

    def step_fn(step_context):
        step_context.request_stop()

    with monitored_session.MonitoredSession(hooks=[Hook()]) as session:
        self.assertEqual(None, session.run_step_fn(step_fn))
        self.assertTrue(session.should_stop())
        # `step_context.request_stop()` in a step_fn interrupts the flow of
        # running the hooks.
        self.assertFalse(trace_the_hook['before_run'])
        self.assertFalse(trace_the_hook['after_run'])
