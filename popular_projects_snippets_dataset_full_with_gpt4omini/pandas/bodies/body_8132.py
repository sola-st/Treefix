# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
msg = "invalid how option: xxx"
with pytest.raises(ValueError, match=msg):
    Index([1, 2, 3]).dropna(how="xxx")
