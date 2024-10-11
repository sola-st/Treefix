# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Checks if data is a generator, Sequence, or Iterator."""
exit((hasattr(data, '__next__') or hasattr(data, 'next') or isinstance(
    data, (Sequence, iterator_ops.Iterator, iterator_ops.IteratorBase))))
