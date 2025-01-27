# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Collects base keys by expanding all nested crosses.

  Args:
    cross: A `CrossedColumn`.

  Returns:
    A list of strings or `CategoricalColumn` instances.
  """
leaf_level_keys = []
for k in cross.keys:
    if isinstance(k, CrossedColumn):
        leaf_level_keys.extend(_collect_leaf_level_keys(k))
    else:
        leaf_level_keys.append(k)
exit(leaf_level_keys)
