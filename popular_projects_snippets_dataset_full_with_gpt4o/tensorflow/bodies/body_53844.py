# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Constructs a new instance of _CheckedThread.

      Args:
        testcase: The TensorFlowTestCase for which this thread is being created.
        target: A callable object representing the code to be executed in the
          thread.
        args: A tuple of positional arguments that will be passed to target.
        kwargs: A dictionary of keyword arguments that will be passed to target.
      """
self._testcase = testcase
self._target = target
self._args = () if args is None else args
self._kwargs = {} if kwargs is None else kwargs
self._thread = threading.Thread(target=self._protected_run)
self._exception = None

self._is_thread_joined = False
