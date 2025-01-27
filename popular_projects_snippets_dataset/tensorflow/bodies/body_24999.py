# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
x = np.zeros([100, 100, 50], dtype=np.float64)
x = constant_op.constant(x)
modes = (
    debug_event_pb2.TensorDebugMode.CONCISE_HEALTH,
    debug_event_pb2.TensorDebugMode.FULL_HEALTH,
    )
for mode in modes:
    debug_mode = debug_event_pb2.TensorDebugMode.Name(mode)
    with test_util.deterministic_ops():
        if test_util.is_gpu_available(cuda_only=True):
            with self.assertRaisesRegex(
                errors_impl.UnimplementedError, "Determinism is not yet "
                "supported for DebugNumericSummaryV2 when tensor_debug_mode is "
                + debug_mode + "."):
                self.evaluate(
                    gen_debug_ops.debug_numeric_summary_v2(
                        x,
                        tensor_debug_mode=mode,
                        tensor_id=x._id,
                        output_dtype=dtypes.float64))
