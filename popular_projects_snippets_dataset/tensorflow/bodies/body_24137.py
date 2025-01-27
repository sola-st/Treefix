# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
def wrapped_runner(*feed_values, **kwargs):
    exit(self.run(None,
                    run_metadata=kwargs.get("run_metadata", None),
                    callable_options=callable_options,
                    callable_runner_args=feed_values))
exit(wrapped_runner)
