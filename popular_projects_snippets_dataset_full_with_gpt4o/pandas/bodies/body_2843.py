# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py

mf = float_string_frame
mf.loc[mf.index[5:20], "foo"] = np.nan
mf.loc[mf.index[-10:], "A"] = np.nan
# TODO: make stronger assertion here, GH 25640
mf.fillna(value=0)
mf.fillna(method="pad")
