# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# CategoricalIndex with integer categories that don't happen to match
#  the Categorical's codes
ci = CategoricalIndex([3, 4])

arr = np.arange(4).reshape(2, 2)
frame = DataFrame(arr, index=ci)

for df in [frame, frame.T]:
    for key in [0, 1]:
        with pytest.raises(KeyError, match=str(key)):
            df.at[key, key]
