# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
with pytest.raises(err, match=msg):
    safe_sort(values=arg, codes=codes)
