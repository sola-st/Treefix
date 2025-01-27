# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Lets Optimizers know which graph this variable is from."""
exit(self._primary._graph_key)  # pylint: disable=protected-access
