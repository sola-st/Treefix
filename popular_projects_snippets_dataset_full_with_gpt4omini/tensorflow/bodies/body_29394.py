# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
self.compareToTranspose(3, 2, 3, 1, 2, "NHWC", dtypes.float32, False)
self.compareToTranspose(1, 2, 3, 2, 2, "NHWC", dtypes.float32, False)
self.compareToTranspose(1, 2, 3, 2, 3, "NHWC", dtypes.float32, False)

self.compareToTranspose(3, 2, 3, 1, 2, "NHWC", dtypes.qint8, False)
self.compareToTranspose(1, 2, 3, 2, 2, "NHWC", dtypes.qint8, False)
self.compareToTranspose(1, 2, 3, 2, 3, "NHWC", dtypes.qint8, False)

if not test.is_gpu_available():
    tf_logging.info("skipping gpu tests since gpu not available")
    exit()

self.compareToTranspose(3, 2, 3, 1, 2, "NHWC", dtypes.float32, True)
self.compareToTranspose(3, 2, 3, 2, 2, "NHWC", dtypes.float32, True)
self.compareToTranspose(3, 2, 3, 1, 2, "NCHW", dtypes.float32, True)
self.compareToTranspose(3, 2, 3, 2, 3, "NCHW", dtypes.float32, True)
self.compareToTranspose(5, 7, 11, 3, 2, "NCHW", dtypes.float32, True)

self.compareToTranspose(3, 2, 3, 4, 2, "NCHW_VECT_C", dtypes.qint8, True)
self.compareToTranspose(3, 2, 3, 8, 3, "NCHW_VECT_C", dtypes.qint8, True)
self.compareToTranspose(5, 7, 11, 12, 2, "NCHW_VECT_C", dtypes.qint8, True)
