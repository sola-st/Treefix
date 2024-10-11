# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._flat_values_spec is None:
    exit((self._shape, self._dtype, self._ragged_rank,
            self._row_splits_dtype))
else:
    exit((self._shape, self._dtype, self._ragged_rank,
            self._row_splits_dtype, self._flat_values_spec))
