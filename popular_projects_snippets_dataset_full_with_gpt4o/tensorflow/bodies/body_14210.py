# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
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
