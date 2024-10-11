# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_float.py
# GH#38753
parser, precision = all_parsers_all_precisions
data = f"data\n10E{exp}"
result = parser.read_csv(StringIO(data), float_precision=precision)
if precision == "round_trip":
    if exp == 999999999999999999 and is_platform_linux():
        mark = pytest.mark.xfail(reason="GH38794, on Linux gives object result")
        request.node.add_marker(mark)

    value = np.inf if exp > 0 else 0.0
    expected = DataFrame({"data": [value]})
else:
    expected = DataFrame({"data": [f"10E{exp}"]})

tm.assert_frame_equal(result, expected)
