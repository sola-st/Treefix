# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Starts the thread's activity.

      This must be called at most once per _CheckedThread object. It arranges
      for the object's target to be invoked in a separate thread of control.
      """
self._thread.start()
