# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
msg = "`color` must be string or list or tuple of 2 strings"
with pytest.raises(ValueError, match=msg):
    df.style.bar(color={"a", "b"}).to_html()
with pytest.raises(ValueError, match=msg):
    df.style.bar(color=["a", "b", "c"]).to_html()

msg = "`color` and `cmap` cannot both be given"
with pytest.raises(ValueError, match=msg):
    df.style.bar(color="something", cmap="something else").to_html()
