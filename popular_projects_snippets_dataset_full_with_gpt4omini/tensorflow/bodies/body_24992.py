# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
modes = [
    debug_event_pb2.TensorDebugMode.CURT_HEALTH,
    debug_event_pb2.TensorDebugMode.CONCISE_HEALTH,
    debug_event_pb2.TensorDebugMode.SHAPE,
]
# Maximum allowed tensor_id
tensor_id = np.power(2, 53, dtype=np.int64)
for mode in modes:
    self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            constant_op.constant(42.0),
            tensor_debug_mode=mode,
            tensor_id=tensor_id,
            output_dtype=dtypes.float64))
# Incrementing by one should error
tensor_id += 1
for mode in modes:
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(
            gen_debug_ops.debug_numeric_summary_v2(
                constant_op.constant(42.0),
                tensor_debug_mode=mode,
                tensor_id=tensor_id,
                output_dtype=dtypes.float64))
