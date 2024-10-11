# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Temporarily stops recording operations on this tape.

    Operations executed while this context manager is active will not be
    recorded on the tape. This is useful for reducing the memory used by tracing
    all computations.

    For example:

    >>> x = tf.constant(4.0)
    >>> with tf.GradientTape() as tape:
    ...   with tape.stop_recording():
    ...     y = x ** 2
    >>> dy_dx = tape.gradient(y, x)
    >>> print(dy_dx)
    None

    Yields:
      None
    Raises:
      RuntimeError: if the tape is not currently recording.
    """
if self._tape is None:
    raise RuntimeError(
        "Trying to stop recording a tape which is not recording.")
self._pop_tape()
try:
    exit()
finally:
    self._push_tape()
