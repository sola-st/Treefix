# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Blocks until the thread terminates.

      Raises:
        self._testcase.failureException: If the thread terminates with due to
          an exception.
      """
self._is_thread_joined = True
self._thread.join()
if self._exception is not None:
    self._testcase.fail("Error in checkedThread: %s" % str(self._exception))
