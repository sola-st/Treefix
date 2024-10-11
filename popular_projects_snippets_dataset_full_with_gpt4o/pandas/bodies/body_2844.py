# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py

# mixed numeric (but no float16)
mf = mixed_float_frame.reindex(columns=["A", "B", "D"])
mf.loc[mf.index[-10:], "A"] = np.nan
result = mf.fillna(value=0)
_check_mixed_float(result, dtype={"C": None})

result = mf.fillna(method="pad")
_check_mixed_float(result, dtype={"C": None})
