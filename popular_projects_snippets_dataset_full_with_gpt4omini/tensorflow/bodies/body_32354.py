# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Check that hann_window matches scipy.signal.hann behavior."""
# The Hann window is a raised cosine window with parameters alpha=0.5 and
# beta=0.5.
# https://en.wikipedia.org/wiki/Window_function#Hann_window
self._compare_window_fns(
    functools.partial(_scipy_raised_cosine, a=0.5, b=0.5),
    window_ops.hann_window, window_length, periodic, tf_dtype_tol)
