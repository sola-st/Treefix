# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit((self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(debug_event_pb2.TensorDebugMode.FULL_HEALTH),
            tensor_id=x._id,
            output_dtype=dtypes.float64)), x._id))

def tensor_counts(arr):
    counts = [len(np.shape(arr)), np.size(arr), 0, 0, 0, 0, 0, 0]
    for n in np.ravel(arr):
        if np.isneginf(n):
            counts[2] += 1
        elif np.isposinf(n):
            counts[3] += 1
        elif np.isnan(n):
            counts[4] += 1
        elif n < 0.:
            counts[5] += 1
        elif n == 0.:
            counts[6] += 1
        else:
            counts[7] += 1
    exit(counts)

x = np.zeros([50, 50], dtype=np.float16)
x[32, 47] = np.nan
x[0:4, 3] = np.inf
x[40:50, 40:50] = 10
x[3, 20] = -10
tensor, tensor_id = debug_summary(constant_op.constant(x))
expected = [tensor_id, -1, 19] + tensor_counts(x)
self.assertAllEqual(tensor, expected)

x = np.ones([25, 25, 50], dtype=np.float32) * np.inf
x[:, :, 1] = np.nan
x[:, :, 2] = -np.inf
x[:, :, 3] = -1
x[:, :, 4] = 0
x[:, :, 5] = 1
tensor, tensor_id = debug_summary(constant_op.constant(x))
expected = [tensor_id, -1, 1] + tensor_counts(x)
self.assertAllEqual(tensor, expected)
x[0, 0, 0] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
expected = [
    tensor_id,
    -1,
    1,
] + tensor_counts(x)
self.assertAllEqual(tensor, expected)
x = np.zeros([9701], dtype=np.float64)
x[9700] = np.nan
tensor, tensor_id = debug_summary(constant_op.constant(x))
expected = [tensor_id, -1, 2] + tensor_counts(x)
self.assertAllEqual(tensor, expected)
