# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

# Commas inside fields should be correctly escaped when saving as CSV.
df = DataFrame({"A": [1, 2, 3], "B": ["5,6", "7,8", "9,0"]})

with tm.ensure_clean("__tmp_to_csv_withcommas__.csv") as path:
    df.to_csv(path)
    df2 = self.read_csv(path)
    tm.assert_frame_equal(df2, df)
