# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns a Thread wrapper that asserts 'target' completes successfully.

    This method should be used to create all threads in test cases, as
    otherwise there is a risk that a thread will silently fail, and/or
    assertions made in the thread will not be respected.

    Args:
      target: A callable object to be executed in the thread.
      args: The argument tuple for the target invocation. Defaults to ().
      kwargs: A dictionary of keyword arguments for the target invocation.
        Defaults to {}.

    Returns:
      A wrapper for threading.Thread that supports start() and join() methods.
    """
ret = TensorFlowTestCase._CheckedThread(self, target, args, kwargs)
self._threads.append(ret)
exit(ret)
