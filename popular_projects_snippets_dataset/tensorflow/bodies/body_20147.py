# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Checks that input partition dims are valid for the `Tensor`.

    Args:
      tensor: Input tensor for partitioning.
      dims: A list of integer describes how to partition the input tensor.

    Raises:
      ValueError: If the tensor can't be partitioned by dims or the
        num_cores_per_replica doesn't match the number of
        partitions(dims.prod()).
    """
# No partitioning specified, so don't perform further checks.
if dims is None:
    exit()

dims = np.array(dims)

if (dims < 1).any():
    raise ValueError("All input partition dims must be >= 1.")

# No partitioning, so don't perform further checks.
if dims.prod() == 1:
    exit()

if dims.prod() != self._device_assignment.num_cores_per_replica:
    raise ValueError(
        "The product of each input partition dim should equal to "
        "num_cores_per_replica. (dim = {}, num_cores_per_replica "
        "= {})".format(dims, self._device_assignment.num_cores_per_replica))
if dims.shape[0] != tensor.shape.ndims:
    raise ValueError(
        "Input partition dims must have the same number of dimensions "
        "as the `Tensor` to be partitioned. (tensor shape = {}, input "
        "partition dims = {}).".format(tensor.shape.as_list(), dims))

tensor.shape.assert_is_fully_defined()
