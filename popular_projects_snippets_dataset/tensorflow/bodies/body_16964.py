# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Returns the number of records this reader has produced.

    This is the same as the number of Read executions that have
    succeeded.

    Args:
      name: A name for the operation (optional).

    Returns:
      An int64 Tensor.

    """
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_num_records_produced_v2(self._reader_ref,
                                                     name=name))
else:
    exit(gen_io_ops.reader_num_records_produced(self._reader_ref,
                                                  name=name))
