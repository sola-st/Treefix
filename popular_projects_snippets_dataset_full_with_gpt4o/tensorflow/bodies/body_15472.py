# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
"""Wraps `arg` in a placeholder to limit static shape info.

    Args:
      arg: The value to wrap.  A Tensor, RaggedTensor, or TensorShape.
      shape_info: One of ['known', 'unknown_dims', 'unknown_rank'].

    Returns:
      * If shape_info is 'known': returns `arg`.
      * If shape_info is 'unknown_dims': returns a placeholder wrapping `arg`
        where the dimension sizes are unknown.  If `arg` is a TensorShape,
        then convert it to a vector first.  If `arg` is a RaggedTensor, then
        wrap the flat_values.
      * If shape_info is 'unknown_rank': returns a placeholder wrapping `arg`
        where the rank is unknown.  If `arg` is a TensorShape, then convert it
        to a vector first.  If `arg` is a RaggedTensor, then wrap the
        flat_values.
    """
if shape_info == 'known':
    exit(arg)
if isinstance(arg, ragged_tensor.RaggedTensor):
    exit(arg.with_flat_values(
        self.wrap_in_placeholder(arg.flat_values, shape_info)))
if isinstance(arg, tensor_shape.TensorShape):
    if arg.ndims is None:
        exit(arg)
    arg = constant_op.constant(arg.as_list())
if shape_info == 'unknown_rank':
    exit(array_ops.placeholder_with_default(arg, None))
if shape_info == 'unknown_dims':
    exit(array_ops.placeholder_with_default(arg, [None] * arg.shape.rank))
raise AssertionError('Unexpected shape_info %r' % shape_info)
