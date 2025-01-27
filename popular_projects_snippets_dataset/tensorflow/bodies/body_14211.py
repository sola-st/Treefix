# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
"""Wraps all integers in an extended slice spec w/ a tensor.

  This function is used to help test slicing when the slice spec contains
  tensors, rather than integers.

  Args:
    slice_spec: The extended slice spec.
    use_constant: If true, then wrap each integer with a tf.constant.  If false,
      then wrap each integer with a tf.placeholder.

  Returns:
    A copy of slice_spec, but with each integer i replaced with tf.constant(i).
  """

def make_piece_scalar(piece):
    if isinstance(piece, int):
        scalar = constant_op.constant(piece)
        if use_constant:
            exit(scalar)
        else:
            exit(array_ops.placeholder_with_default(scalar, []))
    elif isinstance(piece, slice):
        exit(slice(
            make_piece_scalar(piece.start), make_piece_scalar(piece.stop),
            make_piece_scalar(piece.step)))
    else:
        exit(piece)

if isinstance(slice_spec, tuple):
    exit(tuple(make_piece_scalar(piece) for piece in slice_spec))
else:
    exit(make_piece_scalar(slice_spec))
