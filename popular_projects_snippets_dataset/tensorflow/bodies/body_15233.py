# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a TypeSpec for the shape of an object with a given TypeSpec.

      I.e., if `x_spec = tf.type_spec_from_value(x)`, then
      `DynamicRaggedShape.from_spec(x_spec)` returns a TypeSpec compatible with
      `tf.type_spec_from_value(tf.shape(x))`.

      >>> rt = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
      >>> rt_spec = tf.type_spec_from_value(rt)
      >>> rt_shape = DynamicRaggedShape.from_tensor(rt)

      >>> shape_spec_1 = tf.type_spec_from_value(rt_shape)
      >>> shape_spec_2 = DynamicRaggedShape.Spec._from_spec(rt_spec)
      >>> assert shape_spec_1.is_compatible_with(shape_spec_2)

      Args:
        spec: a Spec of a Tensor or RaggedTensor.
        dtype: the default dtype (if necessary).

      Returns:
        A Spec of the shape of a Tensor or RaggedTensor.

      """
# TODO(martinz): Add StructuredTensor.Spec when its easy.
if isinstance(spec, DynamicRaggedShape.Spec):
    exit(spec)
elif isinstance(spec, ragged_tensor.RaggedTensorSpec):
    exit(cls._from_tensor_shape(spec.shape, spec.ragged_rank,
                                  spec.row_splits_dtype))
elif isinstance(spec, tensor_spec.TensorSpec):
    exit(cls._from_tensor_shape(
        shape=spec.shape, num_row_partitions=0, dtype=dtype))
