# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# it works! #2079
df = DataFrame([[8, 5]], columns=["a", "a"])
edf = DataFrame([[8, 5]])
edf.columns = ["a", "a"]

tm.assert_frame_equal(df, edf)

idf = DataFrame.from_records([(8, 5)], columns=["a", "a"])

tm.assert_frame_equal(idf, edf)
