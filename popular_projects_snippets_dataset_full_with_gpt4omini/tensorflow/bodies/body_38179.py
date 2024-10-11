# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_angle = np.angle(cplx)

with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(cplx)
    tf_angle = math_ops.angle(inx)
    tf_angle_val = self.evaluate(tf_angle)

self.assertAllClose(np_angle, tf_angle_val)
self.assertShapeEqual(np_angle, tf_angle)
