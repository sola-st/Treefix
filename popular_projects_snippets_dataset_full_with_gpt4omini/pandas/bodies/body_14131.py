# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py

index = date_range("20130102", periods=6)
s = Series(1, index=index)
result = s.to_string()
assert "2013-01-02" in result

# nat in index
s2 = Series(2, index=[Timestamp("20130111"), NaT])
s = pd.concat([s2, s])
result = s.to_string()
assert "NaT" in result

# nat in summary
result = str(s2.index)
assert "NaT" in result
