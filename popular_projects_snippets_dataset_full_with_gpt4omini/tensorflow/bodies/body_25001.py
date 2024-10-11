# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(
                debug_event_pb2.TensorDebugMode.CONCISE_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

tensor, tensor_id = debug_summary(constant_op.constant([]))
self.assertAllEqual(tensor, [tensor_id, 0.0, 0.0, 0.0, 0.0])

tensor, tensor_id = debug_summary(constant_op.constant(42.0))
self.assertAllEqual(tensor, [tensor_id, 1.0, 0.0, 0.0, 0.0])

tensor, tensor_id = debug_summary(constant_op.constant([3.0, 4.0]))
self.assertAllEqual(tensor, [tensor_id, 2.0, 0.0, 0.0, 0.0])

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([3.0, -np.inf])))
self.assertAllEqual(tensor, [tensor_id, 2.0, 1.0, 0.0, 0.0])

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([[0, 0], [np.nan, 0]])))
self.assertAllEqual(tensor, [tensor_id, 4.0, 0.0, 0.0, 1.0])

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([[0, 0], [np.nan, np.inf]])))
self.assertAllEqual(tensor, [tensor_id, 4.0, 0.0, 1.0, 1.0])

tensor, tensor_id = debug_summary(
    constant_op.constant(np.array([[0, np.inf], [np.nan, -np.inf]])))
self.assertAllEqual(tensor, [tensor_id, 4.0, 1.0, 1.0, 1.0])
