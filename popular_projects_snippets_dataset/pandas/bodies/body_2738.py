# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH 47263: consistent data types for Index and MultiIndex
df = DataFrame(
    {
        1: date_range("2022-01-01", periods=2),
        2: date_range("2022-01-01", periods=2),
        3: date_range("2022-01-01", periods=2),
    }
)

expected = np.rec.array(
    [
        ("2022-01-01", "2022-01-01", "2022-01-01"),
        ("2022-01-02", "2022-01-02", "2022-01-02"),
    ],
    dtype=[
        ("1", f"{tm.ENDIAN}M8[ns]"),
        ("2", f"{tm.ENDIAN}M8[ns]"),
        ("3", f"{tm.ENDIAN}M8[ns]"),
    ],
)

result = df.to_records(index=False)
tm.assert_almost_equal(result, expected)

result = df.set_index(1).to_records(index=True)
tm.assert_almost_equal(result, expected)

result = df.set_index([1, 2]).to_records(index=True)
tm.assert_almost_equal(result, expected)
