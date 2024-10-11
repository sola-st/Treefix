# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# unit test when have object data
with pytest.raises(TypeError, match="Could not convert"):
    float_string_frame.mean(axis=0)

# xs sum mixed type, just want to know it works...
with pytest.raises(TypeError, match="unsupported operand type"):
    float_string_frame.mean(axis=1)

# take mean of boolean column
float_frame["bool"] = float_frame["A"] > 0
means = float_frame.mean(0)
assert means["bool"] == float_frame["bool"].values.mean()
