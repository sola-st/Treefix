# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
df = DataFrame(
    [["one", "two", "three"], ["four", "five", "six"]],
    index=date_range("2012-01-01", "2012-01-02"),
)

expected = df.index.values[0]
result = df.to_records()["index"][0]
assert expected == result
