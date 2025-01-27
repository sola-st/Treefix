# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py

file = datapath("io", "data", "stata", f"{file}.dta")
parsed = self.read_dta(file)

# match stata here
expected = self.read_csv(datapath("io", "data", "stata", "stata3.csv"))
expected = expected.astype(np.float32)
expected["year"] = expected["year"].astype(np.int16)
expected["quarter"] = expected["quarter"].astype(np.int8)

tm.assert_frame_equal(parsed, expected)
