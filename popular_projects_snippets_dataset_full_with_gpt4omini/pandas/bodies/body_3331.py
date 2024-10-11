# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
dfmix = DataFrame(mix_ab)
# the same inplace
# lists of regexes and values
# list of [re1, re2, ..., reN] -> [v1, v2, ..., vN]
to_replace_res = [r"\s*\.\s*", r"a"]
values = [np.nan, "crap"]
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({"a": mix_ab["a"], "b": ["crap", "b", np.nan, np.nan]})
tm.assert_frame_equal(res, expec)

# list of [re1, re2, ..., reN] -> [re1, re2, .., reN]
to_replace_res = [r"\s*(\.)\s*", r"(a|b)"]
values = [r"\1\1", r"\1_crap"]
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({"a": mix_ab["a"], "b": ["a_crap", "b_crap", "..", ".."]})
tm.assert_frame_equal(res, expec)

# list of [re1, re2, ..., reN] -> [(re1 or v1), (re2 or v2), ..., (reN
# or vN)]
to_replace_res = [r"\s*(\.)\s*", r"a", r"(b)"]
values = [r"\1\1", r"crap", r"\1_crap"]
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({"a": mix_ab["a"], "b": ["crap", "b_crap", "..", ".."]})
tm.assert_frame_equal(res, expec)

to_replace_res = [r"\s*(\.)\s*", r"a", r"(b)"]
values = [r"\1\1", r"crap", r"\1_crap"]
res = dfmix.copy()
return_value = res.replace(regex=to_replace_res, value=values, inplace=True)
assert return_value is None
expec = DataFrame({"a": mix_ab["a"], "b": ["crap", "b_crap", "..", ".."]})
tm.assert_frame_equal(res, expec)
