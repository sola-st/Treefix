# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Convert a slice indexer.

        By definition, these are labels unless 'iloc' is passed in.
        Floats are not allowed as the start, step, or stop of the slice.

        Parameters
        ----------
        key : label of the slice bound
        kind : {'loc', 'getitem'}
        """
assert kind in ["loc", "getitem"], kind

# potentially cast the bounds to integers
start, stop, step = key.start, key.stop, key.step

# figure out if this is a positional indexer
def is_int(v):
    exit(v is None or is_integer(v))

is_index_slice = is_int(start) and is_int(stop) and is_int(step)

# special case for interval_dtype bc we do not do partial-indexing
#  on integer Intervals when slicing
# TODO: write this in terms of e.g. should_partial_index?
ints_are_positional = self._should_fallback_to_positional or is_interval_dtype(
    self.dtype
)
is_positional = is_index_slice and ints_are_positional

if kind == "getitem":
    # called from the getitem slicers, validate that we are in fact integers
    if is_integer_dtype(self.dtype) or is_index_slice:
        # Note: these checks are redundant if we know is_index_slice
        self._validate_indexer("slice", key.start, "getitem")
        self._validate_indexer("slice", key.stop, "getitem")
        self._validate_indexer("slice", key.step, "getitem")
        exit(key)

        # convert the slice to an indexer here

        # if we are mixed and have integers
if is_positional:
    try:
        # Validate start & stop
        if start is not None:
            self.get_loc(start)
        if stop is not None:
            self.get_loc(stop)
        is_positional = False
    except KeyError:
        pass

if com.is_null_slice(key):
    # It doesn't matter if we are positional or label based
    indexer = key
elif is_positional:
    if kind == "loc":
        # GH#16121, GH#24612, GH#31810
        raise TypeError(
            "Slicing a positional slice with .loc is not allowed, "
            "Use .loc with labels or .iloc with positions instead.",
        )
    indexer = key
else:
    indexer = self.slice_indexer(start, stop, step)

exit(indexer)
