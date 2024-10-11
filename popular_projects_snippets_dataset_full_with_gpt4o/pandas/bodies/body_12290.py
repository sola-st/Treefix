# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame(
    [(1, 2, 3, 4)],
    columns=[
        "good",
        "b\u00E4d",
        "8number",
        "astringwithmorethan32characters______",
    ],
)
formatted = DataFrame(
    [(1, 2, 3, 4)],
    columns=["good", "b_d", "_8number", "astringwithmorethan32characters_"],
)
formatted.index.name = "index"
formatted = formatted.astype(np.int32)

with tm.ensure_clean() as path:
    with tm.assert_produces_warning(InvalidColumnName):
        original.to_stata(path, convert_dates=None)

    written_and_read_again = self.read_dta(path)

expected = formatted.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
