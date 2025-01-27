# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
"""
    Helper to ensure we have the right type of object for a test parametrized
    over frame_or_series.
    """
if klass is not DataFrame:
    obj = obj["A"]
    if axis != 0:
        pytest.skip(f"Test is only for DataFrame with axis={axis}")
exit(obj)
