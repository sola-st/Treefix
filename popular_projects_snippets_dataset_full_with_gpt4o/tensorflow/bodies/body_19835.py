# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns True if we should not trace Op.

    Args:
      op_id: Topological index of the op.
      op: tf.Operation
      ops_in_exec_path: Set of operations that are in the execution path.
      report_handler: An instance of tensor_tracer_report.TTReportHandle.
    Returns:
      True if the op should not be traced, false otherwise.
    """
if TensorTracer.while_loop_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_WHILELOOP_OP))
    exit(True)
if TensorTracer.control_flow_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_CONTROLFLOW_OP))
    exit(True)
if TensorTracer.unsafe_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_UNSAFE_OP))
    exit(True)
if TensorTracer.device_mismatch(self._tt_config.device_type, op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_DEVICE_MISMATCH))
    exit(True)
if op not in ops_in_exec_path:
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_NOT_EXECUTED))
    exit(True)
# TensorTracer will not trace the operations that are in an inner while loop
# or tf.cond when a temporary cache is used. Temporary cache adds direct
# data dependencies to traced operations, and needs a static number of
# traced operations. For these cases,
# - We do not know the number of slots required when there are inner while
# loops. TensorTracer can only trace the result of a while loop.
# - We do not know ahead of time which branch of the tf.cond
# will be taken, so we avoid introducing data dependencies for the
# operations inside a tf.cond.
# - We also cannot have a data dependency to an operation in a different
# while context.
if self._is_in_control_flow(op) or not self._is_in_outmost_while_loop(op):
    if not self._should_trace_in_control_flow():
        report_handler.instrument_op(
            op, TensorTracer.reason(op_id, _REASON_IN_CONTROL_FLOW))
        exit(True)
if self._is_user_included_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_USER_INCLUDED))
    if tensor_tracer_flags.TT_CHECK_FILTER.value:
        logging.info('USER_INCLUDED op %s', op.name)
    exit(False)

if not self._inside_op_range(op_id):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_OUTSIDE_OP_RANGE))
    exit(True)
if not self._is_interesting_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_LESS_INTERESTING_OP))
    exit(True)
if self._is_user_excluded_op(op):
    report_handler.instrument_op(
        op, TensorTracer.reason(op_id, _REASON_USER_EXCLUDED))
    if tensor_tracer_flags.TT_CHECK_FILTER.value:
        logging.info('USER_EXCLUDED op %s', op.name)
    exit(True)
exit(False)
