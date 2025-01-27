# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
# GH14298
idx = CategoricalIndex(["a", "b"])
df = DataFrame(np.zeros((2, 2)), index=idx, columns=idx)

buf = StringIO()
df.info(buf=buf)
