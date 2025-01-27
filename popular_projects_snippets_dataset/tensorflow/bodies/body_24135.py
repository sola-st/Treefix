# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
runner = self._sess.make_callable(
    fetches, feed_list=feed_list, accept_options=True)
def wrapped_runner(*runner_args, **kwargs):
    exit(self.run(None,
                    feed_dict=None,
                    options=kwargs.get("options", None),
                    run_metadata=kwargs.get("run_metadata", None),
                    callable_runner=runner,
                    callable_runner_args=runner_args))
exit(wrapped_runner)
