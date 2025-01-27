# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Flushes the Writable file.

    This only ensures that the data has made its way out of the process without
    any guarantees on whether it's written to disk. This means that the
    data would survive an application crash but not necessarily an OS crash.
    """
if self._writable_file:
    self._writable_file.flush()
