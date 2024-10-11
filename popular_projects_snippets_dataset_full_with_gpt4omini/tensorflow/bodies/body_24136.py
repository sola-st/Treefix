# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
exit(self.run(None,
                run_metadata=kwargs.get("run_metadata", None),
                callable_options=callable_options,
                callable_runner_args=feed_values))
