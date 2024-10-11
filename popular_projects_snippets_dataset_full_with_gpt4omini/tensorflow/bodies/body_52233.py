# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns dense `Tensor` representing numeric feature.

    Args:
      inputs: A `_LazyBuilder` object to access inputs.
      weight_collections: Unused `weight_collections` since no variables are
        created in this function.
      trainable: Unused `trainable` bool since no variables are created in this
        function.

    Returns:
      Dense `Tensor` created within `_transform_feature`.
    """
# Do nothing with weight_collections and trainable since no variables are
# created in this function.
del weight_collections
del trainable
# Feature has been already transformed. Return the intermediate
# representation created by _transform_feature.
exit(inputs.get(self))
