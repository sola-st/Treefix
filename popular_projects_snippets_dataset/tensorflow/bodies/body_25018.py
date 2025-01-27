# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.FULL_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

# Assert the same op is returns a consistent value
x = np.zeros([100, 100], dtype=np.float16)
x[32, 47] = np.nan
x[0:4, 3] = np.inf
x[90:100, 90:100] = 10
x[3, 20] = -10
c = constant_op.constant(x)
tensor_1, tensor_id_1 = debug_summary(c)
tensor_2, tensor_id_2 = debug_summary(c)
self.assertAllEqual(tensor_1, tensor_2)
self.assertEqual(tensor_id_1, tensor_id_2)

x = np.ones((100, 200, 3, 10), np.double)
x[1, 30, 2] = 10
x[5, :, 0, 1] = np.nan
x[90:100, 150, :, :] = np.inf
c = constant_op.constant(x)
tensor_1, tensor_id_1 = debug_summary(c)
tensor_2, tensor_id_2 = debug_summary(c)
self.assertAllEqual(tensor_1, tensor_2)
self.assertEqual(tensor_id_1, tensor_id_2)
