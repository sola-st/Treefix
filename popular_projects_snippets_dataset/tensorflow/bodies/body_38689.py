# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
np_out = np_func(x)
with self.cached_session(use_gpu=use_gpu) as sess:
    inx = ops.convert_to_tensor(x)
    ofunc = tf_func(inx)
    tf_out = self.evaluate(ofunc)
self.assertAllClose(np_out, tf_out)
