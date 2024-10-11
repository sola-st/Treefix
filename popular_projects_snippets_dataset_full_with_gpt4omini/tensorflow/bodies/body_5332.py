# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.scatter_min(*args, **kwargs))
self._scatter_not_implemented("scatter_min")
