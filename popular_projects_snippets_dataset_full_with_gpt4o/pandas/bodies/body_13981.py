# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_eng_formatting.py
# Issue #11981

formatter = fmt.EngFormatter(accuracy=1, use_eng_prefix=True)
result = formatter(np.inf)
assert result == "inf"
