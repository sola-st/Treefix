# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# see gh-20699
df1 = DataFrame({"isNum": [val]})
df2 = DataFrame({"isBool": [True]})

res = df1.combine_first(df2)
exp = DataFrame({"isBool": [True], "isNum": [val]})

tm.assert_frame_equal(res, exp)
