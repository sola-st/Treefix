# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a `FeatureTransformationCache`.

    Args:
      features: A mapping from feature column to objects that are `Tensor` or
        `SparseTensor`, or can be converted to same via
        `sparse_tensor.convert_to_tensor_or_sparse_tensor`. A `string` key
        signifies a base feature (not-transformed). A `FeatureColumn` key means
        that this `Tensor` is the output of an existing `FeatureColumn` which
        can be reused.
    """
self._features = features.copy()
self._feature_tensors = {}
