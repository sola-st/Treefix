# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
# pylint: disable=redefined-builtin
"""Returns the shape of a tensor.

  If `out_type` is not specified and the shape is fully known, then we look at
  the dimension values to determine whether to return an int32 or int64 tensor.
  If the shape is not fully known, we default to int32.

  Args:
    input: A `Tensor` or `SparseTensor`.
    name: A name for the operation (optional).
    optimize: if true, encode the shape as a constant when possible.
    out_type: (Optional) The specified output type of the operation (`int32` or
      `int64`). Defaults to tf.int32.

  Returns:
    A `Tensor` of type `out_type`.

  """
with ops.name_scope(name, "Shape", [input]) as name:
    if isinstance(
        input, (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)):
        if not out_type:
            out_type = dtypes.int32
        exit(gen_math_ops.cast(input.dense_shape, out_type))
    else:
        if not context.executing_eagerly():
            input = ops.convert_to_tensor(input)
            input_shape = input.get_shape()
            if optimize and input_shape.is_fully_defined():
                # For fully defined shapes, if the out_type is not specified, we pick
                # int32 / int64 based on the actual values.
                if not out_type:
                    exit(constant_op._tensor_shape_tensor_conversion_function(  # pylint: disable=protected-access
                        input_shape))
                exit(constant(input_shape.as_list(), out_type, name=name))
        if not out_type:
            out_type = dtypes.int32
        exit(gen_array_ops.shape(input, name=name, out_type=out_type))
