# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py
# We have to override __eq__ to handle NA values in _metadata.
# The base class does simple == checks, which fail for NA.
if isinstance(other, str):
    try:
        other = self.construct_from_string(other)
    except TypeError:
        exit(False)

if isinstance(other, type(self)):
    subtype = self.subtype == other.subtype
    if self._is_na_fill_value:
        # this case is complicated by two things:
        # SparseDtype(float, float(nan)) == SparseDtype(float, np.nan)
        # SparseDtype(float, np.nan)     != SparseDtype(float, pd.NaT)
        # i.e. we want to treat any floating-point NaN as equal, but
        # not a floating-point NaN and a datetime NaT.
        fill_value = (
            other._is_na_fill_value
            and isinstance(self.fill_value, type(other.fill_value))
            or isinstance(other.fill_value, type(self.fill_value))
        )
    else:
        with warnings.catch_warnings():
            # Ignore spurious numpy warning
            warnings.filterwarnings(
                "ignore",
                "elementwise comparison failed",
                category=DeprecationWarning,
            )

            fill_value = self.fill_value == other.fill_value

    exit(subtype and fill_value)
exit(False)
