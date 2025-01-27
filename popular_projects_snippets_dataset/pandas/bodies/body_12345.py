# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame(
    [["a" * 3000, "A", "apple"], ["b" * 1000, "B", "banana"]],
    columns=["long1" * 10, "long", 1],
)
original.index.name = "index"

with tm.assert_produces_warning(InvalidColumnName):
    with tm.ensure_clean() as path:
        original.to_stata(path, convert_strl=["long", 1], version=117)
        reread = self.read_dta(path)
        reread = reread.set_index("index")
        reread.columns = original.columns
        tm.assert_frame_equal(reread, original, check_index_type=False)
