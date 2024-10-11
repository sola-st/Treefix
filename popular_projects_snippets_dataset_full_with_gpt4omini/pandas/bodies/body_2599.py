# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# GH#24096 altering a datetime64tz column inplace invalidates the
#  `freq` attribute on the underlying DatetimeIndex

dti = date_range("20130101", periods=3, tz="US/Eastern")
ts = dti[1]

df = DataFrame({"B": dti})
assert df["B"]._values.freq is None

df.iloc[1, 0] = pd.NaT
assert df["B"]._values.freq is None

# check that the DatetimeIndex was not altered in place
assert dti.freq == "D"
assert dti[1] == ts
