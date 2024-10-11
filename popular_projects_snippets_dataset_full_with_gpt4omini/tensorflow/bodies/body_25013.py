# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.FULL_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

tensor, tensor_id = debug_summary(constant_op.constant([]))
expected = [tensor_id, -1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(constant_op.constant(42.0))
expected = [tensor_id, -1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(constant_op.constant([3.0, 4.0]))
expected = [tensor_id, -1, 1, 1, 2, 0, 0, 0, 0, 0, 2]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([3, -np.inf], dtype=np.float32)))
expected = [tensor_id, -1, 1, 1, 2, 1, 0, 0, 0, 0, 1]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([[0, 0], [np.nan, 0]], dtype=np.float64)))
expected = [tensor_id, -1, 2, 2, 4, 0, 0, 1, 0, 3, 0]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(
    constant_op.constant(
        np.array([[0, 0], [np.nan, np.inf]], dtype=np.float16)))
expected = [tensor_id, -1, 19, 2, 4, 0, 1, 1, 0, 2, 0]
self.assertAllEqual(tensor, expected)

tensor, tensor_id = debug_summary(
    constant_op.constant(
        np.array([[0, np.inf], [np.nan, -np.inf]], dtype=np.float32)))
expected = [tensor_id, -1, 1, 2, 4, 1, 1, 1, 0, 1, 0]
self.assertAllEqual(tensor, expected)
