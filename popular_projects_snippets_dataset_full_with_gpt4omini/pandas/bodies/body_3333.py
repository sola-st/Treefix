# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# nested dicts will not work until this is implemented for Series
dfmix = DataFrame(mix_abc)
res = dfmix.replace({"b": {r"\s*\.\s*": np.nan}}, regex=True)
res2 = dfmix.copy()
res4 = dfmix.copy()
return_value = res2.replace(
    {"b": {r"\s*\.\s*": np.nan}}, inplace=True, regex=True
)
assert return_value is None
res3 = dfmix.replace(regex={"b": {r"\s*\.\s*": np.nan}})
return_value = res4.replace(regex={"b": {r"\s*\.\s*": np.nan}}, inplace=True)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", "b", np.nan, np.nan], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
tm.assert_frame_equal(res4, expec)
