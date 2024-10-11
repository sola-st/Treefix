# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# insert at the beginning
result = data[1:].insert(0, data[0])
self.assert_extension_array_equal(result, data)

result = data[1:].insert(-len(data[1:]), data[0])
self.assert_extension_array_equal(result, data)

# insert at the middle
result = data[:-1].insert(4, data[-1])

taker = np.arange(len(data))
taker[5:] = taker[4:-1]
taker[4] = len(data) - 1
expected = data.take(taker)
self.assert_extension_array_equal(result, expected)
