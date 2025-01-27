# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.SHAPE),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

x = np.ones([1, 2, 3, 4, 5, 6, 7], dtype=np.double)
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(tensor, [
    tensor_id, 2.0, 7.0, 2 * 3 * 4 * 5 * 6 * 7, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0
])
