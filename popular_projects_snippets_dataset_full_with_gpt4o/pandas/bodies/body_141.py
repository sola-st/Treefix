# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
def _assert_raw(x):
    assert isinstance(x, np.ndarray)
    assert x.ndim == 1

# Mixed dtype (GH-32423)
mixed_type_frame.apply(_assert_raw, axis=axis, raw=True)
