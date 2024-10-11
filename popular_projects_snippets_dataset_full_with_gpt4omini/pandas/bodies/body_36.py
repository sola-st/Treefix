# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
obj = unpack_obj(float_frame, frame_or_series, 0)

with pytest.raises(ValueError, match="No transform functions were provided"):
    obj.transform(ops)
