# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
exit(self.run(None,
                feed_dict=None,
                options=kwargs.get("options", None),
                run_metadata=kwargs.get("run_metadata", None),
                callable_runner=runner,
                callable_runner_args=runner_args))
