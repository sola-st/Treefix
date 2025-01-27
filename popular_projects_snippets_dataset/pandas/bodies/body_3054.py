# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#18580
# When using to_dict(orient='index') on a dataframe with int
# and float columns only the int columns were cast to float

df = DataFrame({"int_col": [1, 2, 3], "float_col": [1.0, 2.0, 3.0]})

result = df.to_dict(orient="index", into=into)
cols = ["int_col", "float_col"]
result = DataFrame.from_dict(result, orient="index")[cols]
expected = DataFrame.from_dict(expected, orient="index")[cols]
tm.assert_frame_equal(result, expected)
