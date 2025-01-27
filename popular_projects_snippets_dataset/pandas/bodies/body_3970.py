# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
with pytest.raises(TypeError, match="unhashable type: 'Index'"):
    float_frame.columns in float_frame
