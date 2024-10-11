# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
value = step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2})
exit(value)
