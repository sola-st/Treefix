# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""A function that destroys the resource."""
exit(self._coordinator_instance._destroy_resource())  # pylint: disable=protected-access
