# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 2909: object conversion to float in constructor?
df = DataFrame(data=[val, "a"])
result = df.applymap(lambda x: x).dtypes[0]
assert result == object
