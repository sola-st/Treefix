# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
f = float_frame
assert f._get_axis_number(0) == 0
assert f._get_axis_number(1) == 1
assert f._get_axis_number("index") == 0
assert f._get_axis_number("rows") == 0
assert f._get_axis_number("columns") == 1

assert f._get_axis_name(0) == "index"
assert f._get_axis_name(1) == "columns"
assert f._get_axis_name("index") == "index"
assert f._get_axis_name("rows") == "index"
assert f._get_axis_name("columns") == "columns"

assert f._get_axis(0) is f.index
assert f._get_axis(1) is f.columns

with pytest.raises(ValueError, match="No axis named"):
    f._get_axis_number(2)

with pytest.raises(ValueError, match="No axis.*foo"):
    f._get_axis_name("foo")

with pytest.raises(ValueError, match="No axis.*None"):
    f._get_axis_name(None)

with pytest.raises(ValueError, match="No axis named"):
    f._get_axis_number(None)
