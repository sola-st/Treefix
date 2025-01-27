# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame(
    data=[["string", "object", 1, 1.1, np.datetime64("2003-12-25")]],
    columns=["string", "object", "integer", "floating", "datetime"],
)
original["object"] = Series(original["object"], dtype=object)
original.index.name = "index"
original.index = original.index.astype(np.int32)
original["integer"] = original["integer"].astype(np.int32)

with tm.ensure_clean() as path:
    original.to_stata(path, convert_dates={"datetime": "tc"}, version=version)
    written_and_read_again = self.read_dta(path)
    # original.index is np.int32, read index is np.int64
    tm.assert_frame_equal(
        written_and_read_again.set_index("index"),
        original,
        check_index_type=False,
    )
