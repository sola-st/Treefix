# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
c = CategoricalIndex(data)
assert c.is_monotonic_increasing is True
assert c.is_monotonic_decreasing is False

c = CategoricalIndex(data, ordered=True)
assert c.is_monotonic_increasing is True
assert c.is_monotonic_decreasing is False

c = CategoricalIndex(data, categories=reversed(data))
assert c.is_monotonic_increasing is False
assert c.is_monotonic_decreasing is True

c = CategoricalIndex(data, categories=reversed(data), ordered=True)
assert c.is_monotonic_increasing is False
assert c.is_monotonic_decreasing is True

# test when data is neither monotonic increasing nor decreasing
reordered_data = [data[0], data[2], data[1]]
c = CategoricalIndex(reordered_data, categories=reversed(data))
assert c.is_monotonic_increasing is False
assert c.is_monotonic_decreasing is False

# non lexsorted categories
categories = non_lexsorted_data

c = CategoricalIndex(categories[:2], categories=categories)
assert c.is_monotonic_increasing is True
assert c.is_monotonic_decreasing is False

c = CategoricalIndex(categories[1:3], categories=categories)
assert c.is_monotonic_increasing is True
assert c.is_monotonic_decreasing is False
