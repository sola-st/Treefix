# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
applied = float_frame.applymap(lambda x: x * 2)
tm.assert_frame_equal(applied, float_frame * 2)
float_frame.applymap(type)

# GH 465: function returning tuples
result = float_frame.applymap(lambda x: (x, x))["A"][0]
assert isinstance(result, tuple)
