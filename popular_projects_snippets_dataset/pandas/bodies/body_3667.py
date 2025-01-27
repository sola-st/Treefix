# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 29136
df = DataFrame(columns=["A", "B"])
msg = r"rename\(\) takes from 1 to 2 positional arguments"

with pytest.raises(TypeError, match=msg):
    df.rename(None, str.lower)
