# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
tf = datetime_frame
tf.loc[tf.index[:5], "A"] = np.nan
tf.loc[tf.index[-5:], "A"] = np.nan

zero_filled = datetime_frame.fillna(0)
assert (zero_filled.loc[zero_filled.index[:5], "A"] == 0).all()

padded = datetime_frame.fillna(method="pad")
assert np.isnan(padded.loc[padded.index[:5], "A"]).all()
assert (
    padded.loc[padded.index[-5:], "A"] == padded.loc[padded.index[-5], "A"]
).all()

msg = "Must specify a fill 'value' or 'method'"
with pytest.raises(ValueError, match=msg):
    datetime_frame.fillna()
msg = "Cannot specify both 'value' and 'method'"
with pytest.raises(ValueError, match=msg):
    datetime_frame.fillna(5, method="ffill")
