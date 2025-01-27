# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#18099
d = {"A": list("abbc"), "B": list("bccd"), "C": list("cdde")}
df = DataFrame(d)
result = df.astype(dtype)
expected = DataFrame({k: Categorical(v, dtype=dtype) for k, v in d.items()})
tm.assert_frame_equal(result, expected)
