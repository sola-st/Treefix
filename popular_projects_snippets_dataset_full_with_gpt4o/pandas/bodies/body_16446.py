# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# GH 13318
values = range(5)
msg = "Bin labels must either be False, None or passed in as a list-like argument"
with pytest.raises(ValueError, match=msg):
    cut(values, 4, labels=labels)
