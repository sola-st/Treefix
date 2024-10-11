# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Check that hamming_window matches scipy.signal.hamming's behavior."""
# The Hamming window is a raised cosine window with parameters alpha=0.54
# and beta=0.46.
# https://en.wikipedia.org/wiki/Window_function#Hamming_window
self._compare_window_fns(
    functools.partial(_scipy_raised_cosine, a=0.54, b=0.46),
    window_ops.hamming_window, window_length, periodic, tf_dtype_tol)
