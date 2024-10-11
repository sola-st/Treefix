# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Call partitioner validating its inputs/output.

  Args:
    partitioner: a function mapping `Tensor` shape and dtype to a list of
      partitions.
    shape: shape of the `Tensor` to partition, must have at least two
      dimensions.
    dtype: dtype of the elements in the `Tensor`.

  Returns:
    A list with elements >=1 and exactly one >1. The index of that
    element corresponds to the partitioning axis.
  """
if not shape.is_fully_defined():
    raise ValueError("Shape of a new partitioned variable must be "
                     "fully defined, but instead was %s." % (shape,))
if shape.ndims < 1:
    raise ValueError("A partitioned Variable must have rank at least 1, "
                     "shape: %s" % shape)

slicing = partitioner(shape=shape, dtype=dtype)
if not isinstance(slicing, collections_abc.Sequence):
    raise ValueError("Partitioner must return a sequence, but saw: %s" %
                     slicing)
if len(slicing) != shape.ndims:
    raise ValueError(
        "Partitioner returned a partition list that does not match the "
        "Variable's rank: %s vs. %s" % (slicing, shape))
if any(p < 1 for p in slicing):
    raise ValueError("Partitioner returned zero partitions for some axes: %s" %
                     slicing)
if sum(p > 1 for p in slicing) > 1:
    raise ValueError("Can only slice a variable along one dimension: "
                     "shape: %s, partitioning: %s" % (shape, slicing))
exit(slicing)
