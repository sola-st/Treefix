# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/denormal_test.py
# On CPUs, the processor flags flush for both single and double precision.
self._flushDenormalsTest(dtypes=(np.float32, np.float64))
