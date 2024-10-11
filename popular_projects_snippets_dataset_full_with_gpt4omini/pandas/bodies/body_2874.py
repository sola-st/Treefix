# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
mf = float_string_frame
mf.loc[mf.index[5:20], "foo"] = np.nan
mf.loc[mf.index[-10:], "A"] = np.nan

filled = float_string_frame.fillna(value=0)
assert (filled.loc[filled.index[5:20], "foo"] == 0).all()
del float_string_frame["foo"]

empty_float = float_frame.reindex(columns=[])

# TODO(wesm): unused?
result = empty_float.fillna(value=0)  # noqa
