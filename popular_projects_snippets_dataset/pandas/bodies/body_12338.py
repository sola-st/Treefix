# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 45350
df = DataFrame({"WithoutInf": [0.0, 1.0], "WithInf": [2.0, infval]})
msg = (
    "Column WithInf contains infinity or -infinity"
    "which is outside the range supported by Stata."
)
with pytest.raises(ValueError, match=msg):
    with tm.ensure_clean() as path:
        df.to_stata(path)
