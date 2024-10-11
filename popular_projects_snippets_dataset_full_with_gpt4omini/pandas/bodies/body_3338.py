# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(mix_abc)
res = df.replace([r"\s*\.\s*", "b"], 0, regex=True)
res2 = df.copy()
return_value = res2.replace([r"\s*\.\s*", "b"], 0, regex=True, inplace=True)
assert return_value is None
res3 = df.copy()
return_value = res3.replace(regex=[r"\s*\.\s*", "b"], value=0, inplace=True)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", 0, 0, 0], "c": ["a", 0, np.nan, "d"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
