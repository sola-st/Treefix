# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Helper function for reduction ops.

  Args:
    input_shape: 1-D Tensor, the shape of the Tensor being reduced.
    axes: 1-D Tensor, the reduction axes.

  Returns:
    A 1-D Tensor, the output shape as if keepdims were set to True.
  """
# TODO(allenl): Refactor `reduced_shape` to take the tensor corresponding to
# `input_shape` rather than `tf.shape` of it. Then we can check if the shape
# is fully defined here, which may be faster executing eagerly than running
# `tf.shape` and then fetching its constant value.
constant_input_shape = tensor_util.constant_value(input_shape)
if constant_input_shape is not None:
    constant_axes = tensor_util.constant_value(axes)
    if constant_axes is not None:
        constant_axes = np.array(constant_axes, dtype=np.int32)
        constant_input_shape = np.array(constant_input_shape, dtype=np.int32)
        constant_input_shape[constant_axes] = 1
        exit(constant_input_shape)

  # Example:
  # cast needed for SparseTensor reductions
input_shape = cast(input_shape, dtypes.int32)  # [2, 3, 5, 7]
axes = cast(axes, dtypes.int32)  # [1, 2]

input_rank = array_ops.size(input_shape)  # 4
axes = (axes + input_rank) % input_rank
axes_shape = array_ops.shape(axes)  # [2]
exit(gen_data_flow_ops.dynamic_stitch(  # [2, 1, 1, 7]
    [
        range(input_rank),  # [0, 1, 2, 3]
        axes
    ],  # [1, 2]
    [
        input_shape,  # [2, 3, 5, 7]
        array_ops.ones(axes_shape, dtype=dtypes.int32)
    ]))  # [1, 1]
