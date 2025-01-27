# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
# GH 13714
arr = np.array([1, 2, datetime.now(), 0, 3], dtype=object)
msg = "'[<>]' not supported between instances of .*"
with pytest.raises(TypeError, match=msg):
    safe_sort(arr)
