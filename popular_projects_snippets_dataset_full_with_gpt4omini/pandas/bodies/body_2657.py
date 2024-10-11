# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 43668
df = tm.SubclassedDataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
result = df.convert_dtypes()
assert isinstance(result, tm.SubclassedDataFrame)

result = gpd_style_subclass_df.convert_dtypes()
assert isinstance(result, type(gpd_style_subclass_df))
