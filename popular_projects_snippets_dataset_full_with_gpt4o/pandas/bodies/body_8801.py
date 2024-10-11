# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if cls is pd.arrays.StringArray:
    msg = "StringArray requires a sequence of strings or pandas.NA"
else:
    msg = "Unsupported type '<class 'numpy.ndarray'>' for ArrowExtensionArray"

with pytest.raises(ValueError, match=msg):
    cls(np.array(["a", "b"], dtype="S1"))

with pytest.raises(ValueError, match=msg):
    cls(np.array([]))

if cls is pd.arrays.StringArray:
    # GH#45057 np.nan and None do NOT raise, as they are considered valid NAs
    #  for string dtype
    cls(np.array(["a", np.nan], dtype=object))
    cls(np.array(["a", None], dtype=object))
else:
    with pytest.raises(ValueError, match=msg):
        cls(np.array(["a", np.nan], dtype=object))
    with pytest.raises(ValueError, match=msg):
        cls(np.array(["a", None], dtype=object))

with pytest.raises(ValueError, match=msg):
    cls(np.array(["a", pd.NaT], dtype=object))

with pytest.raises(ValueError, match=msg):
    cls(np.array(["a", np.datetime64("NaT", "ns")], dtype=object))

with pytest.raises(ValueError, match=msg):
    cls(np.array(["a", np.timedelta64("NaT", "ns")], dtype=object))
