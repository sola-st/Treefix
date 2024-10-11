# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# see gh-14058
exp_msg = "'ordered' must either be 'True' or 'False'"
exp_err = TypeError

# This should be a boolean.
ordered = np.array([0, 1, 2])

with pytest.raises(exp_err, match=exp_msg):
    Categorical([1, 2, 3], ordered=ordered)

with pytest.raises(exp_err, match=exp_msg):
    Categorical.from_codes(
        [0, 0, 1], categories=["a", "b", "c"], ordered=ordered
    )
