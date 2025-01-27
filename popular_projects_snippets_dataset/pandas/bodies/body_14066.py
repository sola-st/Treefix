# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
dm = DataFrame({"c/\u03c3": Series({"test": np.nan})})
str(dm.to_string())
