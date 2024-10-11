# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
result = read_fwf(BytesIO("שלום\nשלום".encode()), widths=[2, 2], encoding="utf8")
expected = DataFrame([["של", "ום"]], columns=["של", "ום"])
tm.assert_frame_equal(result, expected)
