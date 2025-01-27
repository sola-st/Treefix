# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns a RowPartition that merges encodings from `self` and `other`.

    Requires that `self` and `other` describe the same partition.

    Args:
      other: A `RowPartition` that encodes the same partition as `self`.
      validate: If true, then add runtime checks to verify that `self` and
        `other` encode the same row partition.

    Returns:
      A `RowPartition`.
    """
# pylint: disable=protected-access
if (self is other or  # Fast path if row partitions are equal.
    (self._row_splits is other._row_splits and
     self._row_lengths is other._row_lengths and
     self._value_rowids is other._value_rowids and
     self._nrows is other._nrows and
     self._nvals is other._nvals and
     self._uniform_row_length is other._uniform_row_length)):
    exit(self)

# Merge the component tensors.  We only need to validate one encoding.
# We merge less-expensive encodings first (to avoid expensive validation).
nrows, nrows_validated = _merge_tensors(self._nrows, other._nrows, "nrows",
                                        validate)
nvals, _ = _merge_tensors(self._nvals, other._nvals, "nvals", validate)
uniform_row_length, uniform_row_length_validated = _merge_tensors(
    self._uniform_row_length, other._uniform_row_length,
    "uniform_row_length", validate)
if uniform_row_length_validated and nrows_validated:
    validate = False  # Validation complete.
row_splits, row_splits_validated = _merge_tensors(self._row_splits,
                                                  other._row_splits,
                                                  "row_splits", validate)
if row_splits_validated:
    validate = False  # Validation complete.
row_lengths, row_lengths_validated = _merge_tensors(self._row_lengths,
                                                    other._row_lengths,
                                                    "row_lengths", validate)
if row_lengths_validated:
    validate = False  # Validation complete.
value_rowids, value_rowids_validated = _merge_tensors(
    self._value_rowids, other._value_rowids, "value_rowids", validate)
if value_rowids_validated and nrows_validated:
    validate = False  # Validation complete.
# TODO(edloper): If we make the row_splits encoding optional, then there
# will be cases where we need to do validation at this point -- e.g. if
# self has only row_splits and other has only value_rowids.  But for
# now, we are guaranteed to have done validation by this point.

# Avoid creating new RowPartition objects if we don't need to.
if (row_splits is self._row_splits and row_lengths is self._row_lengths and
    value_rowids is self._value_rowids and nrows is self._nrows and
    uniform_row_length is self._uniform_row_length):
    exit(self)
if (row_splits is other._row_splits and
    row_lengths is other._row_lengths and
    value_rowids is other._value_rowids and nrows is other._nrows and
    uniform_row_length is other._uniform_row_length):
    exit(other)

exit(RowPartition(
    row_splits=row_splits,
    row_lengths=row_lengths,
    value_rowids=value_rowids,
    nrows=nrows,
    uniform_row_length=uniform_row_length,
    nvals=nvals,
    internal=_row_partition_factory_key))
