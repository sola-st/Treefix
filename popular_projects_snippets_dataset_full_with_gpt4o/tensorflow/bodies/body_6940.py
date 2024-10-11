# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
if not self._built:
    raise ValueError(
        "Cannot get the cardinality of a dataset that is not built")
exit(self._cardinality)
