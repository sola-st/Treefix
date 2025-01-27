# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# what happens when you try to replace a numeric value with a regex?
df = DataFrame(mix_abc)
res = df.replace(r"\s*\.\s*", 0, regex=True)
res2 = df.copy()
return_value = res2.replace(r"\s*\.\s*", 0, inplace=True, regex=True)
assert return_value is None
res3 = df.copy()
return_value = res3.replace(regex=r"\s*\.\s*", value=0, inplace=True)
assert return_value is None
expec = DataFrame({"a": mix_abc["a"], "b": ["a", "b", 0, 0], "c": mix_abc["c"]})
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
