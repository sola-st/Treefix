# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
empty_frame = DataFrame()

df = DataFrame([1])
msg = "unhashable type: 'DataFrame'"
with pytest.raises(TypeError, match=msg):
    hash(df)
with pytest.raises(TypeError, match=msg):
    hash(empty_frame)
