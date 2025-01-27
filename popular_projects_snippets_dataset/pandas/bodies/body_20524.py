# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
# TODO(GH#50617): once Series.__[gs]etitem__ is removed we should be able
#  to simplify this.
if is_float_dtype(self.dtype):
    assert kind in ["loc", "getitem"]

    # We always treat __getitem__ slicing as label-based
    # translate to locations
    exit(self.slice_indexer(key.start, key.stop, key.step))

exit(super()._convert_slice_indexer(key, kind=kind))
