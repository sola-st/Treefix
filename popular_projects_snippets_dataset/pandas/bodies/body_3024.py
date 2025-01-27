# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH41634
df = DataFrame({"D": [23, 7, 21]})

msg = 'For argument "ascending" expected type bool, received type str.'
with pytest.raises(ValueError, match=msg):
    df.sort_values(by="D", ascending="False")
