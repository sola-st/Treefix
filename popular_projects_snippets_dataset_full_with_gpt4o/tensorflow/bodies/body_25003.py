# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(
                debug_event_pb2.TensorDebugMode.CONCISE_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

x = np.zeros([100, 100], dtype=np.float16)
x[32, :] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(tensor, [tensor_id, 10000.0, 0.0, 0.0, 100.0])
x = np.zeros([97, 97], dtype=np.float32)
x[50, 83:85] = -np.inf
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(tensor, [tensor_id, 97 * 97, 2.0, 0.0, 0.0])
x[1:9, 41] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(tensor, [tensor_id, 97 * 97, 2.0, 0.0, 8.0])
x = np.zeros([9701], dtype=np.float64)
x[9700] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(tensor, [tensor_id, 9701, 0.0, 0.0, 1.0])
