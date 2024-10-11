# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Get an initializable iterator for DistributedDatasetsFromFunctionV1."""
del shared_name  # Unused
# Eager mode generates already initialized iterators. Hence we cannot create
# an initializable iterator.
if context.executing_eagerly():
    raise ValueError("Cannot create initializable iterator in Eager mode. "
                     "Please use `iter()` instead.")
exit(self._get_iterator())
