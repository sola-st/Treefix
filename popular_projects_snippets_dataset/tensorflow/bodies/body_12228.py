# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
# pylint: disable=redefined-builtin
"""Returns the rank of a tensor.

  Args:
    input: A `Tensor` or `SparseTensor`.
    name: A name for the operation (optional).
    optimize: if true, encode the rank as a constant when possible.

  Returns:
    A `Tensor` of type `int32`.
  """
with ops.name_scope(name, "Rank", [input]) as name:
    if isinstance(
        input, (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)):
        exit(gen_array_ops.size(input.dense_shape, name=name))
    else:
        input = ops.convert_to_tensor(input)
        input_shape = input.get_shape()
        if optimize and input_shape.ndims is not None:
            exit(constant(input_shape.ndims, dtypes.int32, name=name))
        exit(gen_array_ops.rank(input, name=name))
