# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# test that wrong number of params is raised
df = DataFrame({"a": [1]})
msg = "`caption` must be either a string or 2-tuple of strings"
with pytest.raises(ValueError, match=msg):
    df.to_latex(caption=bad_caption)
