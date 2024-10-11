# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

def debug_summary(x):
    exit(self.evaluate(
        gen_debug_ops.debug_numeric_summary_v2(
            x,
            tensor_debug_mode=(
                debug_event_pb2.TensorDebugMode.REDUCE_INF_NAN_THREE_SLOTS))))

self.assertAllEqual(
    debug_summary(constant_op.constant([])), [0.0, 0.0, 0.0])
self.assertAllEqual(
    debug_summary(constant_op.constant(42.0)), [0.0, 0.0, 0.0])
self.assertAllEqual(
    debug_summary(constant_op.constant([3.0, 4.0])), [0.0, 0.0, 0.0])
self.assertAllEqual(
    debug_summary(constant_op.constant(np.array([3.0, -np.inf]))),
    [-np.inf, 0.0, 0.0])
self.assertAllEqual(
    debug_summary(constant_op.constant(np.array([[0, 0], [np.nan, 0]]))),
    [0.0, 0.0, np.nan])
self.assertAllEqual(
    debug_summary(
        constant_op.constant(np.array([[0, 0], [np.nan, np.inf]]))),
    [0.0, np.inf, np.nan])
self.assertAllEqual(
    debug_summary(
        constant_op.constant(np.array([[0, np.inf], [np.nan, -np.inf]]))),
    [-np.inf, np.inf, np.nan])

x = np.zeros([100, 100], dtype=np.float16)
x[32, 47] = np.nan
self.assertAllEqual(
    debug_summary(constant_op.constant(x)), [0.0, 0.0, np.nan])
x = np.zeros([97, 97], dtype=np.float32)
x[50, 83] = -np.inf
self.assertAllEqual(
    debug_summary(constant_op.constant(x)), [-np.inf, 0.0, 0.0])
x[1, 41] = np.nan
self.assertAllEqual(
    debug_summary(constant_op.constant(x)), [-np.inf, 0.0, np.nan])
x = np.zeros([9701], dtype=np.float64)
x[9700] = np.nan
self.assertAllEqual(
    debug_summary(constant_op.constant(x)), [0.0, 0.0, np.nan])
