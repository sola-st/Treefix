# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Returns the number of work units this reader has finished processing.

    Args:
      name: A name for the operation (optional).

    Returns:
      An int64 Tensor.
    """
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_num_work_units_completed_v2(self._reader_ref,
                                                         name=name))
else:
    exit(gen_io_ops.reader_num_work_units_completed(self._reader_ref,
                                                      name=name))
