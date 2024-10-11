# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Produce a string tensor that encodes the state of a reader.

    Not all Readers support being serialized, so this can produce an
    Unimplemented error.

    Args:
      name: A name for the operation (optional).

    Returns:
      A string Tensor.
    """
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_serialize_state_v2(self._reader_ref, name=name))
else:
    exit(gen_io_ops.reader_serialize_state(self._reader_ref, name=name))
