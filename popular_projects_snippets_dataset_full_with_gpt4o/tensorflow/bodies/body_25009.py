# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.SHAPE),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

x = np.zeros([3, 4], dtype=np.float32)
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(
    tensor, [tensor_id, 1.0, 2.0, 12.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0])

x = np.ones([1, 2, 3, 4, 5, 6], dtype=np.float16)
x[0, 1, 2, 2, 2, 2] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(
    tensor,
    [tensor_id, 19, 6.0, 2 * 3 * 4 * 5 * 6, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

x = np.zeros([2], dtype=np.float32)
tensor, tensor_id = debug_summary(constant_op.constant(x))
self.assertAllEqual(
    tensor, [tensor_id, 1.0, 1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0])

tensor, tensor_id = debug_summary(constant_op.constant([]))
self.assertAllEqual(
    tensor, [tensor_id, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
