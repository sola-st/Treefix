# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
exit(tensor_shape.TensorShape(
    tuple(self.source_column.shape) + (len(self.boundaries) + 1,)))
