# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_min, np_max = np.minimum(x, y), np.maximum(x, y)
with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    omin, omax = math_ops.minimum(inx, iny), math_ops.maximum(inx, iny)
    tf_min, tf_max = self.evaluate([omin, omax])
self.assertAllEqual(np_min, tf_min)
self.assertAllEqual(np_max, tf_max)
