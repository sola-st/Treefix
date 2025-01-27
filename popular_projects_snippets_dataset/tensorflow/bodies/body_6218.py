# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Shortcut for `tf.group(self.experimental_local_results(value))`."""
exit(self._extended._group(value, name))  # pylint: disable=protected-access
