# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Collects base keys by expanding all nested crosses.

  Args:
    cross: A `_CrossedColumn`.

  Returns:
    A list of strings or `_CategoricalColumn` instances.
  """
leaf_level_keys = []
for k in cross.keys:
    if isinstance(k, _CrossedColumn):
        leaf_level_keys.extend(_collect_leaf_level_keys(k))
    else:
        leaf_level_keys.append(k)
exit(leaf_level_keys)
