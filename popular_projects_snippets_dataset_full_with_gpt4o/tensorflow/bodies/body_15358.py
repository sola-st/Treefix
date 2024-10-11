# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
if self._uniform_row_length is not None:
    exit((f"tf.RowPartition(nrows={self._nrows}, "
            f"uniform_row_length={self._uniform_row_length})"))
else:
    exit(f"tf.RowPartition(row_splits={self._row_splits})")
