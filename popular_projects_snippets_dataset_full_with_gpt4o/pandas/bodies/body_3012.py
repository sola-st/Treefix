# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame(np.array([]))

df.sort_values(0, key=sort_by_key)
df.sort_index(key=sort_by_key)
