# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns True if we should not trace out_tensor.

    Args:
      op_id: Topological index of the op producing tensor.
      out_tensor: tf.Tensor
      report_handler: An instance of tensor_tracer_report.TTReportHandle.
    Returns:
      True if the tensor should not be traced, false otherwise.
    """

# Skips a tensor if the tensor has a non-numeric type.
#   Note: we cannot use check_ops.is_numeric_tensor(out_tensor)
#         because it also excludes tensors with dtypes, bool, and
#         float32_ref, which we actually want to trace.
non_numeric_tensor_types = set([dtypes.variant, dtypes.resource,
                                dtypes.string])
if out_tensor.dtype in non_numeric_tensor_types:

    report_handler.instrument_tensor(
        out_tensor, TensorTracer.reason(op_id, _REASON_NON_NUMERIC_TENSOR))
    exit(True)
# Skip a tensor if it feeds a special while loop op.
if [consumer for consumer in out_tensor.consumers() if
    TensorTracer.while_loop_op(consumer)]:
    report_handler.instrument_tensor(
        out_tensor, TensorTracer.reason(op_id, _REASON_FEEDS_WHILELOOP_OP))
    exit(True)
if self._is_user_included_op(out_tensor.op):
    report_handler.instrument_tensor(
        out_tensor, TensorTracer.reason(op_id, _REASON_USER_INCLUDED))
    if tensor_tracer_flags.TT_CHECK_FILTER.value:
        logging.info('USER_INCLUDED tensor %s', out_tensor.name)
    exit(False)
if self._is_user_excluded_op(out_tensor.op):
    report_handler.instrument_tensor(
        out_tensor, TensorTracer.reason(op_id, _REASON_USER_EXCLUDED))
    if tensor_tracer_flags.TT_CHECK_FILTER.value:
        logging.info('USER_EXCLUDED tensor %s', out_tensor.name)
    exit(True)
if not out_tensor.get_shape().is_fully_defined():
    # If trace mode is nan-inf, norm or max, then the tensor will be reduced
    # to a scalar before the outside compilation call.
    if self._parameters.trace_mode in (
        tensor_tracer_flags.TRACE_MODE_NAN_INF,
        tensor_tracer_flags.TRACE_MODE_NORM,
        tensor_tracer_flags.TRACE_MODE_HISTORY,
        tensor_tracer_flags.TRACE_MODE_MAX_ABS,
        tensor_tracer_flags.TRACE_MODE_SUMMARY
        ):
        report_handler.instrument_tensor(
            out_tensor, TensorTracer.reason(op_id, _REASON_TENSOR_GET_TRACED))
        exit(False)
    else:
        report_handler.instrument_tensor(
            out_tensor, TensorTracer.reason(op_id, _REASON_DYNAMIC_SHAPE))
        exit(True)
rank = len(out_tensor.shape)
if rank < 1:
    # scalar
    if self._parameters.trace_scalar_ops:
        if TensorTracer.unsafe_scalar_trace(out_tensor.op):
            report_handler.instrument_tensor(
                out_tensor, TensorTracer.reason(op_id, _REASON_UNSAFE_SCALAR))
            exit(True)
        else:
            report_handler.instrument_tensor(
                out_tensor, TensorTracer.reason(op_id, _REASON_SCALAR_GET_TRACED))
            exit(False)
    else:
        report_handler.instrument_tensor(
            out_tensor, TensorTracer.reason(op_id, _REASON_SKIP_SCALAR))
        exit(True)
else:
    # tensor
    report_handler.instrument_tensor(
        out_tensor, TensorTracer.reason(op_id, _REASON_TENSOR_GET_TRACED))
    exit(False)
