# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
np_ans = np_func(x, y)
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = tf_func(inx, iny)
    tf_gpu = self.evaluate(out)
self.assertAllClose(np_ans, tf_gpu)
self.assertShapeEqual(np_ans, out)
