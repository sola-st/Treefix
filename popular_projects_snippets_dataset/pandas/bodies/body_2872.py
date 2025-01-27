# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# list
msg = '"value" parameter must be a scalar or dict, but you passed a "{}"'
with pytest.raises(TypeError, match=msg.format("list")):
    float_frame.fillna([1, 2])
# tuple
with pytest.raises(TypeError, match=msg.format("tuple")):
    float_frame.fillna((1, 2))
# frame with series
msg = (
    '"value" parameter must be a scalar, dict or Series, but you '
    'passed a "DataFrame"'
)
with pytest.raises(TypeError, match=msg):
    float_frame.iloc[:, 0].fillna(float_frame)
