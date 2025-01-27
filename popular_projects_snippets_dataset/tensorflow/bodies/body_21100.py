# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
trace_the_exception['side_effect_counter'] += 1
step_context.session.run(graph_side_effect)
exit(step_context.run_with_hooks(fetches=v, feed_dict={c: 1.3}))
