# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
data = datapath("io", "data", "html", "wikipedia_states.html")
result = self.read_html(data, match="Arizona", index_col=0)[0]
assert result.shape == (60, 11)
assert "Unnamed" in result.columns[-1][1]
assert result.columns.nlevels == 2
assert np.allclose(result.loc["Alaska", ("Total area[2]", "sq mi")], 665384.04)
