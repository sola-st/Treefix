# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Check if vorbis windows satisfy MDCT window conditions."""
self._check_mdct_window(window_ops.vorbis_window(window_length,
                                                 dtype=tf_dtype_tol[0]),
                        tol=tf_dtype_tol[1])
