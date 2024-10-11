# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#34789
df = DataFrame({"Y0": [1, 2], "Y1": [3, 4]})
result = df.replace({"replace_string": "test"})

tm.assert_frame_equal(result, df)

result = df["Y0"].replace({"replace_string": "test"})
tm.assert_series_equal(result, df["Y0"])
