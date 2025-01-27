# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
file = datapath("io", "data", "stata", f"{file}.dta")
parsed = self.read_dta(file)
parsed.index.name = "index"

tm.assert_frame_equal(parsed_114, parsed)

with tm.ensure_clean() as path:
    parsed_114.to_stata(path, convert_dates={"date_td": "td"}, version=version)
    written_and_read_again = self.read_dta(path)

expected = parsed_114.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
