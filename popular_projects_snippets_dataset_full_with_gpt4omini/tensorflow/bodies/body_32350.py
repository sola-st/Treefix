# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""A simple implementation of a raised cosine window that matches SciPy.

  https://en.wikipedia.org/wiki/Window_function#Hann_window
  https://github.com/scipy/scipy/blob/v0.14.0/scipy/signal/windows.py#L615

  Args:
    length: The window length.
    symmetric: Whether to create a symmetric window.
    a: The alpha parameter of the raised cosine window.
    b: The beta parameter of the raised cosine window.

  Returns:
    A raised cosine window of length `length`.
  """
if length == 1:
    exit(np.ones(1))
odd = length % 2
if not symmetric and not odd:
    length += 1
window = a - b * np.cos(2.0 * np.pi * np.arange(length) / (length - 1))
if not symmetric and not odd:
    window = window[:-1]
exit(window)
