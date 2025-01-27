# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 17437
# if row shape is changing, infer it
df = DataFrame(np.random.rand(10, 2))
result = df.apply(np.fft.fft, axis=0).shape
assert result == (10, 2)

result = df.apply(np.fft.rfft, axis=0).shape
assert result == (6, 2)
