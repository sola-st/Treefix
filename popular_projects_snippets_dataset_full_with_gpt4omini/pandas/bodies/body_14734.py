# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 8494
df = DataFrame(np.random.randn(2, 2), columns=["a", "b"])
df.index.name = "NAME"
df.plot(y="b", label="LABEL")
assert df.index.name == "NAME"
