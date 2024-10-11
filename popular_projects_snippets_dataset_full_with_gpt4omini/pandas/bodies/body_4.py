# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=["a", "a", "c"])
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.apply(lambda x: x, 2)
