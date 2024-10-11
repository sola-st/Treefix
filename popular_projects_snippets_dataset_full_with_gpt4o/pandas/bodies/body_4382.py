# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
nitems = 100
nums = list(range(nitems))
random.shuffle(nums)
expected = [f"A{i:d}" for i in nums]
df = DataFrame(OrderedDict(zip(expected, [[0]] * nitems)))
assert expected == list(df.columns)
