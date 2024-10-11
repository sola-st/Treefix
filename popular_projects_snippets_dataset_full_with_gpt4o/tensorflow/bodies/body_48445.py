# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Add a variable that can hold state which is updated during adapt().

    Args:
      name: Variable name.
      shape: Variable shape. Defaults to scalar if unspecified.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      initializer: initializer instance (callable).
      partitioner: Partitioner to be passed to the `Trackable` API.
      use_resource: Whether to use `ResourceVariable`
      **kwargs: Additional keyword arguments. Accepted values are `getter` and
        `collections`.

    Returns:
      The created variable.
    """
weight = self.add_weight(
    name=name,
    shape=shape,
    dtype=dtype,
    initializer=initializer,
    regularizer=None,
    trainable=False,
    constraint=None,
    partitioner=partitioner,
    use_resource=use_resource,
    **kwargs)
# TODO(momernick): Do not allow collisions here.
self.state_variables[name] = weight
exit(weight)
