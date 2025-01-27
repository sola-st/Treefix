# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Organizes columns into a features dictionary.

    Args:
      *columns: list of `Tensor`s corresponding to one csv record.
    Returns:
      An OrderedDict of feature names to values for that particular record. If
      label_name is provided, extracts the label feature to be returned as the
      second element of the tuple.
    """
features = collections.OrderedDict(zip(column_names, columns))
if label_name is not None:
    label = features.pop(label_name)
    exit((features, label))
exit(features)
