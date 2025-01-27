# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Check for error when random_state argument invalid.
msg = (
    "random_state must be an integer, array-like, a BitGenerator, Generator, "
    "a numpy RandomState, or None"
)
with pytest.raises(ValueError, match=msg):
    obj.sample(random_state="a_string")
