# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a Sharding that splits a tensor across a dimension.

    This creates a Tiled attribute, similar to tile(), but easier to use for the
    common case of tiling a tensor N ways in one dimension.

    Args:
      tensor: A tf.Tensor to split.
      split_dimension: The dimension number to split.
      num_devices: The number of cores to split `tensor` over.
      input_shape: The shape of the original tensor.

    Raises:
      ValueError: The tensor to split was smaller in the split dimension than
        the number of devices to split over.
    """
if input_shape:
    shape = input_shape
else:
    shape = tensor.shape.as_list()
if (shape[split_dimension] is not None and
    shape[split_dimension] < num_devices):
    raise ValueError('Split dimension was smaller than the required number '
                     'of splits: shape=%r, dimension=%r, num_devices=%r' %
                     (shape, split_dimension, num_devices))

tile_assignment_dims = [1] * len(shape)
tile_assignment_dims[split_dimension] = num_devices

exit(Sharding(
    proto=xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.OTHER,
        tile_assignment_dimensions=tile_assignment_dims,
        tile_assignment_devices=range(num_devices))))
