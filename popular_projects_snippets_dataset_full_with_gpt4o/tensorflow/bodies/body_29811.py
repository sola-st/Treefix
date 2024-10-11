# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
self.compareToTranspose(3, 2, 3, 1, 2, "NHWC", False)
self.compareToTranspose(3, 2, 3, 2, 2, "NHWC", False)
self.compareToTranspose(1, 2, 3, 2, 3, "NHWC", False)

if not test.is_gpu_available():
    tf_logging.info("skipping gpu tests since gpu not available")
    exit()

self.compareToTranspose(3, 2, 3, 1, 2, "NHWC", True)
self.compareToTranspose(3, 2, 3, 2, 2, "NHWC", True)
self.compareToTranspose(3, 2, 3, 1, 2, "NCHW", True)
self.compareToTranspose(3, 2, 3, 2, 2, "NCHW", True)
self.compareToTranspose(3, 2, 3, 1, 3, "NCHW", True)
self.compareToTranspose(3, 2, 3, 2, 3, "NCHW", True)
self.compareToTranspose(5, 7, 11, 3, 2, "NCHW", True)
self.compareToTranspose(3, 200, 300, 32, 2, "NCHW", True)

self.compareToTranspose(3, 2, 3, 8, 2, "NCHW_VECT_C", True)
self.compareToTranspose(3, 2, 3, 4, 3, "NCHW_VECT_C", True)
self.compareToTranspose(3, 2, 3, 8, 3, "NCHW_VECT_C", True)
self.compareToTranspose(5, 7, 11, 12, 2, "NCHW_VECT_C", True)
self.compareToTranspose(3, 200, 300, 32, 2, "NCHW_VECT_C", True)
