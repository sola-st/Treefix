# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Force all buffered modifications to be written to disk.

        Parameters
        ----------
        fsync : bool (default False)
          call ``os.fsync()`` on the file handle to force writing to disk.

        Notes
        -----
        Without ``fsync=True``, flushing may not guarantee that the OS writes
        to disk. With fsync, the operation will block until the OS claims the
        file has been written; however, other caching layers may still
        interfere.
        """
if self._handle is not None:
    self._handle.flush()
    if fsync:
        with suppress(OSError):
            os.fsync(self._handle.fileno())
