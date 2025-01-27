# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 39211 - some ops don't support axis=1
df = DataFrame({"a": [1, 2], "b": [3, 4]})
msg = f"Operation {how} does not support axis=1"
with pytest.raises(ValueError, match=msg):
    df.apply(how, axis=1, args=args)
