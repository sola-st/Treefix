# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.array([["x_0_0", "x_0_1", "x_0_2"], ["x_1_0", "x_1_1", "x_1_2"],
              ["x_2_0", "x_2_1", "x_2_2"]],
             dtype=np.object_)
y = np.array([["y_0_0", "y_0_1", "y_0_2"], ["y_1_0", "y_1_1", "y_1_2"],
              ["y_2_0", "y_2_1", "y_2_2"]],
             dtype=np.object_)
z = np.array([["z_0", "z_1", "z_2"]], dtype=np.object_)
w = np.array("w", dtype=np.object_)
self._compareCpu(x, y, _ADD, _ADD)
self._compareCpu(x, z, _ADD, _ADD)
self._compareCpu(x, w, _ADD, _ADD)
self._compareCpu(z, w, _ADD, _ADD)
