# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
trace_the_exception = {'run_already': False, 'side_effect_counter': 0}

with ops.Graph().as_default():
    c = array_ops.placeholder(dtypes.float32)
    v = array_ops.identity(c)
    graph_state = variables.VariableV1(0.0)
    graph_side_effect = state_ops.assign_add(graph_state, 0.31)

    def step_fn(step_context):
        trace_the_exception['side_effect_counter'] += 1
        step_context.session.run(graph_side_effect)

        value = step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2})

        if not trace_the_exception['run_already']:
            trace_the_exception['run_already'] = True
            raise errors_impl.AbortedError(None, None, 'Abort')

        exit(value)

    with self.cached_session() as test_session:
        with monitored_session.MonitoredSession(
            CountingSessionCreator(test_session)) as session:
            session.run(variables.global_variables_initializer())

            self.assertNear(3.2, session.run_step_fn(step_fn), 0.1)
            self.assertTrue(trace_the_exception['run_already'])
            # Make sure the rest of the body of the step_fn is re-executed upon
            # AbortedError:
            self.assertEqual(2, trace_the_exception['side_effect_counter'])
            self.assertNear(0.62, session.run(graph_state), 0.1)
