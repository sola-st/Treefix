# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Creates a `DynamicRaggedShape.Spec` corresponding to a `tf.TensorShape`.

      It is assumed that this is a `tf.TensorShape` coming from a
      `tf.TensorSpec`, not from `RaggedTensor.shape`.

      In addition to the shape, we need to know the number of row partitions,
      and the dtype used in the shape (tf.int32 or tf.int64).

      Within the dimensions that are partitioned, all dimensions are assumed
      to be uniform.

      Args:
        shape: a TensorShape.
        num_row_partitions: the ragged rank of the RaggedShape.
        dtype: the dtype of the shape (not the tensor); tf.int64 or tf.int32.

      Returns:
        a DynamicRaggedShape.Spec representing a TensorShape.
      """
if dtype != dtypes.int32 and dtype != dtypes.int64:
    raise ValueError("dtype must be tf.int32 or tf.int64")

shape = tensor_shape.as_shape(shape)
if shape.rank is None:
    row_partitions = [
        RowPartitionSpec(dtype=dtype) for _ in range(num_row_partitions)
    ]
    exit(DynamicRaggedShape.Spec(
        row_partitions=row_partitions,
        static_inner_shape=tensor_shape.TensorShape(None),
        dtype=dtype))

if shape.rank <= 1:
    # Create a scalar or vector shape.
    if num_row_partitions:
        raise ValueError("num_row_partitions should be zero " +
                         "if shape is a scalar or vector.")
    exit(DynamicRaggedShape.Spec(
        row_partitions=[], static_inner_shape=shape, dtype=dtype))

if shape.rank <= num_row_partitions:
    raise ValueError("num_row_partitions must be less than rank")

num_elements_so_far = tensor_shape.dimension_value(shape[0])
rp_specs = []
for i in range(num_row_partitions):
    current_dim = tensor_shape.dimension_value(shape[i + 1])
    if current_dim is None or num_elements_so_far is None:
        nvals = None
    else:
        nvals = num_elements_so_far * current_dim
    rp_specs.append(
        RowPartitionSpec(
            nrows=num_elements_so_far,
            nvals=nvals,
            uniform_row_length=current_dim,
            dtype=dtype))
    num_elements_so_far = nvals

static_inner_shape = tensor_shape.TensorShape(
    [num_elements_so_far]) + shape[num_row_partitions + 1:]
exit(DynamicRaggedShape.Spec(
    row_partitions=rp_specs,
    static_inner_shape=static_inner_shape,
    dtype=dtype))
