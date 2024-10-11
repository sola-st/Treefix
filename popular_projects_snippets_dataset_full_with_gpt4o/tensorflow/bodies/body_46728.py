# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
assert isinstance(other, set)
result = _NodeState(self)
for s in other:
    result.value.pop(s, None)
exit(result)
