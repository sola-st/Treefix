# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
if test.is_built_with_rocm():
    exit(self._np_fft(r2c.astype(np_rtype), rank, fft_length))
else:
    exit(c2r.astype(np_ctype))
