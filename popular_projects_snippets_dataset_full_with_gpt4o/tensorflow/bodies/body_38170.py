# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_floor, np_ceil = np.floor(x), np.ceil(x)

inx = ops.convert_to_tensor(x)
ofloor, oceil = math_ops.floor(inx), math_ops.ceil(inx)
tf_floor, tf_ceil = self.evaluate([ofloor, oceil])

self.assertAllEqual(np_floor, tf_floor)
self.assertAllEqual(np_ceil, tf_ceil)
self.assertShapeEqual(np_floor, ofloor)
self.assertShapeEqual(np_ceil, oceil)
