# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/denormal_test.py
# On GPUs, only single precision can flush to zero.
self._flushDenormalsTest(dtypes=(np.float32,))
