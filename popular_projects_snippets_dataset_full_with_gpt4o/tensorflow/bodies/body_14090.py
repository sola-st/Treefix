# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Create a structured tensor with the shape of a dense tensor."""
# Note: If a tensor will have rank 0,
# it either has a fully defined shape or has unknown rank.
if t.shape.is_fully_defined():
    exit(StructuredTensor.from_fields({}, shape=t.shape))
elif t.shape.rank is None:
    raise ValueError("Can't build StructuredTensor w/ unknown rank")
elif t.shape.rank == 1:
    exit(StructuredTensor.from_fields({}, shape=t.shape,
                                        nrows=array_ops.shape(t)[0]))
else:
    rt = ragged_tensor.RaggedTensor.from_tensor(t)
    exit(_structured_tensor_from_row_partitions(t.shape,
                                                  rt._nested_row_partitions))
