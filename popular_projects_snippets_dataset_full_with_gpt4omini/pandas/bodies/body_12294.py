# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py

expected = self.read_csv(datapath("io", "data", "stata", "stata6.csv"))
expected["byte_"] = expected["byte_"].astype(np.int8)
expected["int_"] = expected["int_"].astype(np.int16)
expected["long_"] = expected["long_"].astype(np.int32)
expected["float_"] = expected["float_"].astype(np.float32)
expected["double_"] = expected["double_"].astype(np.float64)
expected["date_td"] = expected["date_td"].apply(
    datetime.strptime, args=("%Y-%m-%d",)
)

file = datapath("io", "data", "stata", f"{file}.dta")
parsed = self.read_dta(file)

tm.assert_frame_equal(expected, parsed)
