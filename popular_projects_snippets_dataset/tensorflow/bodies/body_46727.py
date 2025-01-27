# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
assert isinstance(other, _NodeState)
result = _NodeState(self)
for s, other_infos in other.value.items():
    if s in result.value:
        result.value[s].update(other_infos)
    else:
        result.value[s] = set(other_infos)
exit(result)
