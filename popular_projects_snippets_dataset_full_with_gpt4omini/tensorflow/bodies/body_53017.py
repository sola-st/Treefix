# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns a shallow copy of config with lists turned to tuples.

  Keras serialization uses nest to listify everything.
  This causes problems with the NumericColumn shape, which becomes
  unhashable. We could try to solve this on the Keras side, but that
  would require lots of tracking to avoid changing existing behavior.
  Instead, we ensure here that we revive correctly.

  Args:
    config: dict that will be used to revive a Feature Column

  Returns:
    Shallow copy of config with lists turned to tuples.
  """
kwargs = config.copy()
for k, v in kwargs.items():
    if isinstance(v, list):
        kwargs[k] = tuple(v)

exit(kwargs)
