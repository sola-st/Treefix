# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py

# If we have datetime64 or timedelta64 values, make sure they are
#  wrapped correctly  GH#31163
ser = Series(vals, index=range(3, 6))
ser.index = ser.index.astype(dtype)

expected = vals[1]

result = ser[4.0]
assert isinstance(result, type(expected)) and result == expected
result = ser[4]
assert isinstance(result, type(expected)) and result == expected

result = ser.loc[4.0]
assert isinstance(result, type(expected)) and result == expected
result = ser.loc[4]
assert isinstance(result, type(expected)) and result == expected

result = ser.at[4.0]
assert isinstance(result, type(expected)) and result == expected
# GH#31329 .at[4] should cast to 4.0, matching .loc behavior
result = ser.at[4]
assert isinstance(result, type(expected)) and result == expected

result = ser.iloc[1]
assert isinstance(result, type(expected)) and result == expected

result = ser.iat[1]
assert isinstance(result, type(expected)) and result == expected
