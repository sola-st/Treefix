# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Create the metadata.

    Args:
      sparse: Python boolean.
      map_op: The `Operation` that created the `SparseTensorsMap` in question.
        This Op contains information about the underlying Map object and the
        dtype of the original data.
      rank: The statically known rank of the `SparseTensor`.
    """
self._sparse = sparse
self._map_op = map_op
self._rank = tensor_shape.as_dimension(rank)
