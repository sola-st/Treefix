# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
init = tf.initializers.uniform_unit_scaling(0.5, seed=1)
self.assertArrayNear(
    [-0.45200047, 0.72815341],
    init((2,)).numpy(),
    err=1e-6)
