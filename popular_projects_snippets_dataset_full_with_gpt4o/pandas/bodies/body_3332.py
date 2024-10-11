# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
dfmix = DataFrame(mix_abc)

# dicts
# single dict {re1: v1}, search the whole frame
# need test for this...

# list of dicts {re1: v1, re2: v2, ..., re3: v3}, search the whole
# frame
res = dfmix.replace({"b": r"\s*\.\s*"}, {"b": np.nan}, regex=True)
res2 = dfmix.copy()
return_value = res2.replace(
    {"b": r"\s*\.\s*"}, {"b": np.nan}, inplace=True, regex=True
)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", "b", np.nan, np.nan], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)

# list of dicts {re1: re11, re2: re12, ..., reN: re1N}, search the
# whole frame
res = dfmix.replace({"b": r"\s*(\.)\s*"}, {"b": r"\1ty"}, regex=True)
res2 = dfmix.copy()
return_value = res2.replace(
    {"b": r"\s*(\.)\s*"}, {"b": r"\1ty"}, inplace=True, regex=True
)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", "b", ".ty", ".ty"], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)

res = dfmix.replace(regex={"b": r"\s*(\.)\s*"}, value={"b": r"\1ty"})
res2 = dfmix.copy()
return_value = res2.replace(
    regex={"b": r"\s*(\.)\s*"}, value={"b": r"\1ty"}, inplace=True
)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": ["a", "b", ".ty", ".ty"], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)

# scalar -> dict
# to_replace regex, {value: value}
expec = DataFrame(
    {"a": mix_abc["a"], "b": [np.nan, "b", ".", "."], "c": mix_abc["c"]}
)
res = dfmix.replace("a", {"b": np.nan}, regex=True)
res2 = dfmix.copy()
return_value = res2.replace("a", {"b": np.nan}, regex=True, inplace=True)
assert return_value is None
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)

res = dfmix.replace("a", {"b": np.nan}, regex=True)
res2 = dfmix.copy()
return_value = res2.replace(regex="a", value={"b": np.nan}, inplace=True)
assert return_value is None
expec = DataFrame(
    {"a": mix_abc["a"], "b": [np.nan, "b", ".", "."], "c": mix_abc["c"]}
)
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
