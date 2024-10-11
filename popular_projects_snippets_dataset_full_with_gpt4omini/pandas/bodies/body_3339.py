# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(mix_abc)
s1 = Series({"b": r"\s*\.\s*"})
s2 = Series({"b": np.nan})
res = df.replace(s1, s2, regex=True)
res2 = df.copy()
return_value = res2.replace(s1, s2, inplace=True, regex=True)
assert return_value is None
res3 = df.copy()
return_value = res3.replace(regex=s1, value=s2, inplace=True)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", "b", np.nan, np.nan], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
