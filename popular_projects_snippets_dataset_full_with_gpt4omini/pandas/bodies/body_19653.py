# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
self._axes = axes
self.arrays = arrays

if verify_integrity:
    assert len(axes) == 1
    assert len(arrays) == 1
    self._axes = [ensure_index(ax) for ax in self._axes]
    arr = arrays[0]
    arr = maybe_coerce_values(arr)
    arr = extract_pandas_array(arr, None, 1)[0]
    self.arrays = [arr]
    self._verify_integrity()
