# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_bar.py
df = DataFrame({"A": [-100, -60, -30, -20]})

msg = "`align` should be in {'left', 'right', 'mid', 'mean', 'zero'} or"
with pytest.raises(ValueError, match=msg):
    df.style.bar(align="poorly", color=["#d65f5f", "#5fba7d"]).to_html()

msg = r"`width` must be a value in \[0, 100\]"
with pytest.raises(ValueError, match=msg):
    df.style.bar(width=200).to_html()

msg = r"`height` must be a value in \[0, 100\]"
with pytest.raises(ValueError, match=msg):
    df.style.bar(height=200).to_html()
