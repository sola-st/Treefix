# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
exit({
    self.key:
        parsing_ops.FixedLenFeature(self.shape, self.dtype,
                                    self.default_value)
})
