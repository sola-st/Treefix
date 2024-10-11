# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Restore a reader to a previously saved state.

    Not all Readers support being restored, so this can produce an
    Unimplemented error.

    Args:
      state: A string Tensor.
        Result of a SerializeState of a Reader with matching type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_restore_state_v2(
        self._reader_ref, state, name=name))
else:
    exit(gen_io_ops.reader_restore_state(self._reader_ref, state, name=name))
