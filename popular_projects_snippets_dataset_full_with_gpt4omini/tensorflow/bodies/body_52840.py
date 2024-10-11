# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns bucketized categorical `source_column` tensor."""
source_tensor = transformation_cache.get(self.source_column, state_manager)
exit(math_ops._bucketize(  # pylint: disable=protected-access
    source_tensor,
    boundaries=self.boundaries))
