# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(["A", "B", "B", "C", "A"])
msg = (
    'For argument "inplace" expected type bool, '
    f"received type {type(value).__name__}"
)

with pytest.raises(ValueError, match=msg):
    cat.sort_values(inplace=value)
