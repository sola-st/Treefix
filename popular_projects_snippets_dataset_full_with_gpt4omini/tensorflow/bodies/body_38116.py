# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np.logical_not(x)
with test_util.device(use_gpu=use_gpu):
    out = math_ops.logical_not(ops.convert_to_tensor(x))
    tf_val = self.evaluate(out)
self.assertEqual(out.dtype, dtypes_lib.bool)
self.assertAllEqual(np_ans, tf_val)
self.assertShapeEqual(np_ans, out)
