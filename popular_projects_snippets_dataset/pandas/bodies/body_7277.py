# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
idx = TimedeltaIndex(["4day", "1day", "2day"], name="idx")

item = np.datetime64("NaT")
result = idx.insert(0, item)

expected = Index([item] + list(idx), dtype=object, name="idx")
tm.assert_index_equal(result, expected)

# Also works if we pass a different dt64nat object
item2 = np.datetime64("NaT")
result = idx.insert(0, item2)
tm.assert_index_equal(result, expected)
