# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
exit(gen_debug_ops.debug_numeric_summary_v2(
    x,
    tensor_debug_mode=(
        debug_event_pb2.TensorDebugMode.REDUCE_INF_NAN_THREE_SLOTS)))
