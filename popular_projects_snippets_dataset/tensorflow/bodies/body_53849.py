# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns whether the checked thread was properly used and did terminate.

      Every checked thread should be "join"ed after starting, and before the
      test tears down. If it is not joined, it is possible the thread will hang
      and cause flaky failures in tests.

      Raises:
        self._testcase.failureException: If check_termination was called before
        thread was joined.

        RuntimeError: If the thread is not terminated. This means thread was not
        joined with the main thread.
      """
if self._is_thread_joined:
    if self.is_alive():
        raise RuntimeError(
            "Thread was not joined with main thread, and is still running "
            "when the test finished.")
else:
    self._testcase.fail("A checked thread was not joined.")
