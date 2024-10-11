# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = tf_func(inx, iny)
    tf_gpu = self.evaluate(out)

with self.cached_session(use_gpu=False):
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = tf_func(inx, iny)
    tf_cpu = self.evaluate(out)

self.assertAllClose(tf_cpu, tf_gpu)
