# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np_func(x, y)
with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = tf_func(inx, iny)
    tf_val = self.evaluate(out)
self.assertEqual(out.dtype, dtypes_lib.bool)
self.assertAllEqual(np_ans, tf_val)
self.assertShapeEqual(np_ans, out)
