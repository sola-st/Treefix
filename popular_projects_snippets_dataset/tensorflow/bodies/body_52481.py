# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
exit({
    self.name:
        parsing_ops.VarLenFeature(dtypes.int32),
    '{}_weights'.format(self.name):
        parsing_ops.VarLenFeature(dtypes.float32),
})
