# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
r"""Closes the file.

    Should be called for the WritableFile to be flushed.

    In general, if you use the context manager pattern, you don't need to call
    this directly.

    >>> with tf.io.gfile.GFile("/tmp/x", "w") as f:
    ...   f.write("asdf\n")
    ...   f.write("qwer\n")
    >>> # implicit f.close() at the end of the block

    For cloud filesystems, forgetting to call `close()` might result in data
    loss as last write might not have been replicated.
    """
self._read_buf = None
if self._writable_file:
    self._writable_file.close()
    self._writable_file = None
