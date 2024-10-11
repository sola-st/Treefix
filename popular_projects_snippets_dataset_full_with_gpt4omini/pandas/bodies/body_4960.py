# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
"""
        Cases where ``Series.argmax`` and related should raise an exception
        """
msg = (
    "reduction operation 'argmin' not allowed for this dtype|"
    "attempt to get argmin of an empty sequence"
)
with pytest.raises(error_type, match=msg):
    test_input.idxmin()
with pytest.raises(error_type, match=msg):
    test_input.idxmin(skipna=False)
msg = (
    "reduction operation 'argmax' not allowed for this dtype|"
    "attempt to get argmax of an empty sequence"
)
with pytest.raises(error_type, match=msg):
    test_input.idxmax()
with pytest.raises(error_type, match=msg):
    test_input.idxmax(skipna=False)
