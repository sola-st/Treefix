# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    # uint8, uint16
    self._convert([0, 255 * 256], dtypes.uint16, dtypes.uint8, [0, 255])
    self._convert([0, 255], dtypes.uint8, dtypes.uint16, [0, 255 * 256])
    # int8, uint16
    self._convert([0, 127 * 2 * 256], dtypes.uint16, dtypes.int8, [0, 127])
    self._convert([0, 127], dtypes.int8, dtypes.uint16, [0, 127 * 2 * 256])
    # int16, uint16
    self._convert([0, 255 * 256], dtypes.uint16, dtypes.int16, [0, 255 * 128])
    self._convert([0, 255 * 128], dtypes.int16, dtypes.uint16, [0, 255 * 256])
