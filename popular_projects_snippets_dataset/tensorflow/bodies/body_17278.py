# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Make sure converting from and to a float type scales appropriately
with self.cached_session():
    self._convert([0, 1, 255], dtypes.uint8, dtypes.float32,
                  [0, 1.0 / 255.0, 1])
    self._convert([0, 1.1 / 255.0, 1], dtypes.float32, dtypes.uint8,
                  [0, 1, 255])
