# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
assert isinstance(other, _TypeMap)
result = _TypeMap(self)
for s, other_types in other.types.items():
    if s not in result.types:
        self_types = set()
        result.types[s] = self_types
    else:
        self_types = result.types[s]
    self_types.update(other_types)
exit(result)
