# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
for dtype in [
    dtypes.bool, dtypes.double, dtypes.complex64, dtypes.float32,
    dtypes.float64, dtypes.qint16, dtypes.qint32
]:
    with self.assertRaises(TypeError):
        _ = dataset_ops.Dataset.from_generator(lambda: [], dtype).unique()
