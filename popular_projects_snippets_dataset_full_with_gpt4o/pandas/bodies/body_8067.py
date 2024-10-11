# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([1, 2, 3])
default_dict = defaultdict(lambda: "blank")
default_dict[1] = "stuff"
result = index.map(default_dict)
expected = Index(["stuff", "blank", "blank"])
tm.assert_index_equal(result, expected)
