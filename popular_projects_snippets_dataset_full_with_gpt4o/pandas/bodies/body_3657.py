# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
float_frame.rename(columns={"C": "foo"})
assert "C" in float_frame
assert "foo" not in float_frame

c_values = float_frame["C"]
float_frame = float_frame.copy()
return_value = float_frame.rename(columns={"C": "foo"}, inplace=True)
assert return_value is None

assert "C" not in float_frame
assert "foo" in float_frame
# GH 44153
# Used to be id(float_frame["foo"]) != c_id, but flaky in the CI
assert float_frame["foo"] is not c_values
