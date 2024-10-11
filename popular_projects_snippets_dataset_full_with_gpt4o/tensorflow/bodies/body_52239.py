# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
# By construction, source_column is always one-dimensional.
exit((len(self.boundaries) + 1) * self.source_column.shape[0])
