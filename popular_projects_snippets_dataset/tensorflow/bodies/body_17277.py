# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Make sure converting to between float types does nothing interesting
with self.cached_session():
    self._convert([-1.0, 0, 1.0, 200000], dtypes.float32, dtypes.float64,
                  [-1.0, 0, 1.0, 200000])
    self._convert([-1.0, 0, 1.0, 200000], dtypes.float64, dtypes.float32,
                  [-1.0, 0, 1.0, 200000])
