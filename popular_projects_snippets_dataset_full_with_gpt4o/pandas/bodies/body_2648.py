# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py

df = tm.SubclassedDataFrame(
    {"num_legs": [2, 4], "num_wings": [2, 0]}, index=["falcon", "dog"]
)
result = df.isin([0, 2])
assert isinstance(result, tm.SubclassedDataFrame)
