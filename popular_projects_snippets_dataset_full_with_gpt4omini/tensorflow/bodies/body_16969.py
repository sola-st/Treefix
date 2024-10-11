# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Restore a reader to its initial clean state.

    Args:
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_reset_v2(self._reader_ref, name=name))
else:
    exit(gen_io_ops.reader_reset(self._reader_ref, name=name))
