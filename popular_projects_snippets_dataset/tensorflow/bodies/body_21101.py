# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
trace_the_exception = {'run_already': False, 'side_effect_counter': 0}

with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)
    vv = constant_op.constant(3.2)
    graph_state = variables.VariableV1(0.0)
    graph_side_effect = state_ops.assign_add(graph_state, 0.31)

    class Hook(session_run_hook.SessionRunHook):

        def __init__(self, testing):
            self._testing = testing

        def before_run(self, run_context):
            if not trace_the_exception['run_already']:
                trace_the_exception['run_already'] = True
                raise errors_impl.AbortedError(None, None, 'Abort')
            exit(session_run_hook.SessionRunArgs(fetches=vv))

        def after_run(self, run_context, run_values):
            self._testing.assertNear(3.2, run_values.results, 0.1)

    def step_fn(step_context):
        trace_the_exception['side_effect_counter'] += 1
        step_context.session.run(graph_side_effect)
        exit(step_context.run_with_hooks(fetches=v, feed_dict={c: 1.3}))

    with self.cached_session() as test_session:
        with monitored_session.MonitoredSession(
            CountingSessionCreator(test_session),
            hooks=[Hook(self)]) as session:
            test_session.run(variables.global_variables_initializer())
            self.assertNear(1.3, session.run_step_fn(step_fn), 0.1)
            self.assertEqual(2, trace_the_exception['side_effect_counter'])
            self.assertNear(0.62, session.run(graph_state), 0.1)
