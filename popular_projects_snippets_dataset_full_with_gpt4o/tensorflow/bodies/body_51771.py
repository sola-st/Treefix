# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

class NotAFeatureColumn(object):
    pass

builder = _LazyBuilder(features={'a': [[2], [3.]]})
with self.assertRaisesRegex(
    TypeError, '"key" must be either a "str" or "_FeatureColumn".'):
    builder.get(NotAFeatureColumn())
