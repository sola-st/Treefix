# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
data = datapath("io", "data", "html", "wikipedia_states.html")
assert os.path.isfile(data), f"{repr(data)} is not a file"
assert os.path.getsize(data), f"{repr(data)} is an empty file"
result = self.read_html(data, match="Arizona", header=1)[0]
assert result.shape == (60, 12)
assert "Unnamed" in result.columns[-1]
assert result["sq mi"].dtype == np.dtype("float64")
assert np.allclose(result.loc[0, "sq mi"], 665384.04)
