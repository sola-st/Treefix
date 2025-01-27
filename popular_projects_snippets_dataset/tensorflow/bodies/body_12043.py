# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for MatrixSetDiagV2."""
diag_shape = op.inputs[1].get_shape()
if not diag_shape.is_fully_defined():
    # Need to know the values of `d_lower` and `d_upper` to infer diag_shape.
    grad_shape = array_ops.shape(grad)
    batch_shape = grad_shape[:-2]
    matrix_shape = grad_shape[-2:]
    diag_index = array_ops.reshape(op.inputs[2], [-1])  # Converts to vector.
    d_lower = diag_index[0]
    d_upper = diag_index[-1]  # Works both when len(diag_index) is 1 and 2.
    y_offset = control_flow_ops.cond(
        math_ops.less(d_upper, 0), lambda: d_upper, lambda: 0)
    x_offset = control_flow_ops.cond(
        math_ops.greater(d_lower, 0), lambda: -d_lower, lambda: 0)

    max_diag_len = math_ops.minimum(matrix_shape[0] + y_offset,
                                    matrix_shape[1] + x_offset)
    # pylint: disable=g-long-lambda
    # pyformat: disable
    postfix = control_flow_ops.cond(
        math_ops.equal(d_lower, d_upper),
        lambda: ops.convert_to_tensor([max_diag_len]),
        lambda: ops.convert_to_tensor([d_upper - d_lower + 1,
                                       max_diag_len]))
    # pyformat: enable
    # pylint: enable=g-long-lambda
    diag_shape = array_ops.concat([batch_shape, postfix], 0)

grad_input = array_ops.matrix_set_diag(
    grad, array_ops.zeros(diag_shape, dtype=grad.dtype), k=op.inputs[2])
grad_diag = array_ops.matrix_diag_part(grad, k=op.inputs[2])
exit((grad_input, grad_diag, None))
