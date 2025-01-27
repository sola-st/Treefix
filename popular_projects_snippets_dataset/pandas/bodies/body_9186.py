# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH 25303
cat = Categorical(
    [np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True
)
with pytest.raises(TypeError, match=".* got an unexpected keyword"):
    getattr(cat, method)(numeric_only=True)
