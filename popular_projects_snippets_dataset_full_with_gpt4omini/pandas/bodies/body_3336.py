# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(mix_abc)
expec = DataFrame(
    {
        "a": mix_abc["a"],
        "b": np.array([np.nan] * 4),
        "c": [np.nan, np.nan, np.nan, "d"],
    }
)
res = df.replace([r"\s*\.\s*", "a|b"], np.nan, regex=True)
res2 = df.copy()
res3 = df.copy()
return_value = res2.replace(
    [r"\s*\.\s*", "a|b"], np.nan, regex=True, inplace=True
)
assert return_value is None
return_value = res3.replace(
    regex=[r"\s*\.\s*", "a|b"], value=np.nan, inplace=True
)
assert return_value is None
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
