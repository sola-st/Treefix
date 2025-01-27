# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
data = [
    OrderedDict([["a", 1.5], ["b", 3], ["c", 4], ["d", 6]]),
    OrderedDict([["a", 1.5], ["b", 3], ["d", 6]]),
    OrderedDict([["a", 1.5], ["d", 6]]),
    OrderedDict(),
    OrderedDict([["a", 1.5], ["b", 3], ["c", 4]]),
    OrderedDict([["b", 3], ["c", 4], ["d", 6]]),
]

result = DataFrame(data)
expected = DataFrame.from_dict(
    dict(zip(range(len(data)), data)), orient="index"
)
tm.assert_frame_equal(result, expected.reindex(result.index))
