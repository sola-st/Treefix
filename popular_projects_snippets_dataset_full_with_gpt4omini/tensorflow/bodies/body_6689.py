# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.scatter_mul(*args, **kwargs))
raise NotImplementedError
