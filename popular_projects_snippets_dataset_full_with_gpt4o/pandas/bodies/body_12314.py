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

no_conversion = read_stata(
    datapath("io", "data", "stata", "stata6_117.dta"), convert_dates=True
)
tm.assert_frame_equal(expected, no_conversion)

conversion = read_stata(
    datapath("io", "data", "stata", "stata6_117.dta"),
    convert_dates=True,
    preserve_dtypes=False,
)

# read_csv types are the same
expected = self.read_csv(datapath("io", "data", "stata", "stata6.csv"))
expected["date_td"] = expected["date_td"].apply(
    datetime.strptime, args=("%Y-%m-%d",)
)

tm.assert_frame_equal(expected, conversion)
