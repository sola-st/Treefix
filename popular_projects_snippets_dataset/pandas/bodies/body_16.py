# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH39025
df = DataFrame({"a": ["1"]})
msg = r"Column\(s\) \[1, 'b'\] do not exist"
with pytest.raises(KeyError, match=msg):
    df.transform({"a": int, 1: str, "b": int})
