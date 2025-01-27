# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
"""Raises an exception if there are new Python objects created.

    It computes the number of new Python objects per type using the first and
    the last snapshots.

    Args:
      threshold: A dictionary of [Type name string], [count] pair. It won't
        raise an exception if the new Python objects are under this threshold.
    """
self._python_memory_checker.assert_no_new_objects(threshold=threshold)
