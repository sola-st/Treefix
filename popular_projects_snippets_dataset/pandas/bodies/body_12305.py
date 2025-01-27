# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
columns = ["tc", "td", "tw", "tm", "tq", "th", "ty"]
conversions = {c: c for c in columns}
data = [datetime(2006, 11, 20, 23, 13, 20)] * len(columns)
original = DataFrame([data], columns=columns)
original.index.name = "index"
expected_values = [
    datetime(2006, 11, 20, 23, 13, 20),  # Time
    datetime(2006, 11, 20),  # Day
    datetime(2006, 11, 19),  # Week
    datetime(2006, 11, 1),  # Month
    datetime(2006, 10, 1),  # Quarter year
    datetime(2006, 7, 1),  # Half year
    datetime(2006, 1, 1),
]  # Year

expected = DataFrame(
    [expected_values],
    index=pd.Index([0], dtype=np.int32, name="index"),
    columns=columns,
)

with tm.ensure_clean() as path:
    original.to_stata(path, convert_dates=conversions)
    written_and_read_again = self.read_dta(path)

tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
