# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
obj = tm.box_expected(dt64_series, box_with_array)

msg = "cannot perform .* with this index type"

# multiplication
with pytest.raises(TypeError, match=msg):
    obj * one
with pytest.raises(TypeError, match=msg):
    one * obj

# division
with pytest.raises(TypeError, match=msg):
    obj / one
with pytest.raises(TypeError, match=msg):
    one / obj
