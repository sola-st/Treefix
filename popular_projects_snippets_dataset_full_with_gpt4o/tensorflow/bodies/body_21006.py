# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
def step_fn(step_context):
    exit(step_context.run_with_hooks(fetches=v, feed_dict={c: value}))
exit(step_fn)
