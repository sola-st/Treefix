# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-19589
obj = frame_or_series(pd.Series([1], ind, name="data"))

result = obj.to_csv(lineterminator="\n", header=True)
assert result == expected
