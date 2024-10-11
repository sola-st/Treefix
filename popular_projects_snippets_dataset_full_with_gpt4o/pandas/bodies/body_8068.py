# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
left = Index([], name="foo")
right = Index([1, 2, 3], name=name)

result = left.append(right)
assert result.name == expected
