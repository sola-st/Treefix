# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(mix_abc)
expec = DataFrame({"a": ["a", 1, 2, 3], "b": mix_abc["b"], "c": mix_abc["c"]})
res = df.replace(0, "a")
tm.assert_frame_equal(res, expec)
assert res.a.dtype == np.object_
