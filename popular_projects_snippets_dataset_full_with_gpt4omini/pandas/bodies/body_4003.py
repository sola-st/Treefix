# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py

# this may fail on certain platforms because of a numpy issue
# related GH#6140
if not is_platform_little_endian():
    pytest.skip("known failure of test on non-little endian")

# construction with a null in a recarray
# GH#6140
expected = DataFrame({"EXPIRY": [datetime(2005, 3, 1, 0, 0), None]})

arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
dtypes = [("EXPIRY", "<M8[ns]")]

recarray = np.core.records.fromarrays(arrdata, dtype=dtypes)

result = DataFrame.from_records(recarray)
tm.assert_frame_equal(result, expected)

# coercion should work too
arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
dtypes = [("EXPIRY", "<M8[m]")]
recarray = np.core.records.fromarrays(arrdata, dtype=dtypes)
result = DataFrame.from_records(recarray)
# we get the closest supported unit, "s"
expected["EXPIRY"] = expected["EXPIRY"].astype("M8[s]")
tm.assert_frame_equal(result, expected)
