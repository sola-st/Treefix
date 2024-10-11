# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
exit((self.evaluate(
    gen_debug_ops.debug_numeric_summary_v2(
        x,
        tensor_debug_mode=(debug_event_pb2.TensorDebugMode.SHAPE),
        tensor_id=x._id,
        output_dtype=dtypes.float64)), x._id))
