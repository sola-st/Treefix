# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 19861
# edited for GH 33562
if (
    isinstance(slice_[-1], tuple)
    and isinstance(slice_[-1][-1], list)
    and "C" in slice_[-1][-1]
):
    ctx = pytest.raises(KeyError, match="C")
elif (
    isinstance(slice_[0], tuple)
    and isinstance(slice_[0][1], list)
    and 3 in slice_[0][1]
):
    ctx = pytest.raises(KeyError, match="3")
else:
    ctx = contextlib.nullcontext()

idx = MultiIndex.from_product([["a", "b"], [1, 2]])
col = MultiIndex.from_product([["x", "y"], ["A", "B"]])
df = DataFrame(np.random.rand(4, 4), columns=col, index=idx)

with ctx:
    df.style.applymap(lambda x: "color: red;", subset=slice_).to_html()
