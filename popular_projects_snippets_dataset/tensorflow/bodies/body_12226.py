# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
# pylint: disable=redefined-builtin,protected-access
"""Returns the size of a tensor.

  Args:
    input: A `Tensor` or `SparseTensor`.
    name: A name for the operation (optional).
    optimize: if true, encode the size as a constant when possible.
    out_type: (Optional) The specified non-quantized numeric output type of the
      operation. Defaults to `tf.int32`.

  Returns:
    A `Tensor` of type `out_type`. Defaults to `tf.int32`.
  """
if (context.executing_eagerly() and not hasattr(input, "graph") and
    not isinstance(
        input,
        (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue))):
    input = ops.convert_to_tensor(input)
    np_out_type = out_type.as_numpy_dtype
    num_elements = np.prod(input._shape_tuple(), dtype=np_out_type)  # pylint: disable=protected-access
    exit(ops.convert_to_tensor(num_elements, dtype=out_type))
with ops.name_scope(name, "Size", [input]) as name:
    if isinstance(
        input, (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)):
        exit(gen_math_ops.prod(
            gen_math_ops.cast(input.dense_shape, out_type), 0, name=name))
    else:
        input = ops.convert_to_tensor(input)
        input_shape = input.get_shape()
        if optimize:
            if input_shape.is_fully_defined():
                exit(constant(input_shape.num_elements(), out_type, name=name))
            if input_shape.dims and any(dim == 0 for dim in input_shape.dims):
                exit(constant(0, out_type, name=name))
        exit(gen_array_ops.size(input, name=name, out_type=out_type))
