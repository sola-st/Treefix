# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Make sure converting to between integer types scales appropriately
with self.cached_session():
    self._convert([0, 255], dtypes.uint8, dtypes.int16, [0, 255 * 128])
    self._convert([0, 32767], dtypes.int16, dtypes.uint8, [0, 255])
    self._convert([0, 2**32], dtypes.int64, dtypes.int32, [0, 1])
    self._convert([0, 1], dtypes.int32, dtypes.int64, [0, 2**32])
