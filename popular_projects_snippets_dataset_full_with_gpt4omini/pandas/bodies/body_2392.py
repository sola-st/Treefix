# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

float_frame["E"] = "foo"
data = float_frame[["A", "B"]]
float_frame[["B", "A"]] = data

tm.assert_series_equal(float_frame["B"], data["A"], check_names=False)
tm.assert_series_equal(float_frame["A"], data["B"], check_names=False)

msg = "Columns must be same length as key"
with pytest.raises(ValueError, match=msg):
    data[["A"]] = float_frame[["A", "B"]]
newcolumndata = range(len(data.index) - 1)
msg = (
    rf"Length of values \({len(newcolumndata)}\) "
    rf"does not match length of index \({len(data)}\)"
)
with pytest.raises(ValueError, match=msg):
    data["A"] = newcolumndata
