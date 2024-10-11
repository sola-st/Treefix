# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.CURT_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

x = np.zeros([100, 100], dtype=np.float16)
x[43, 99] = np.nan
c = constant_op.constant(x)
tensor_1, tensor_id_1 = debug_summary(c)
tensor_2, tensor_id_2 = debug_summary(c)
self.assertAllEqual(tensor_1, tensor_2)
self.assertEqual(tensor_id_1, tensor_id_2)

x = np.zeros([100, 100, 50], dtype=np.float64)
x[0, 0, 1] = np.inf
c = constant_op.constant(x)
tensor_1, tensor_id_1 = debug_summary(c)
tensor_2, tensor_id_2 = debug_summary(c)
self.assertAllEqual(tensor_1, tensor_2)
self.assertEqual(tensor_id_1, tensor_id_2)

c = constant_op.constant(np.ones((100, 200), np.double))
tensor_1, tensor_id_1 = debug_summary(c)
tensor_2, tensor_id_2 = debug_summary(c)
self.assertAllEqual(tensor_1, tensor_2)
self.assertEqual(tensor_id_1, tensor_id_2)
