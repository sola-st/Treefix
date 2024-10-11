# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
with pytest.raises(TypeError, match="could not convert"):
    float_string_frame.std(1)
with pytest.raises(TypeError, match="could not convert"):
    float_string_frame.var(1)
with pytest.raises(TypeError, match="unsupported operand type"):
    float_string_frame.mean(1)
with pytest.raises(TypeError, match="could not convert"):
    float_string_frame.skew(1)
