# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
if frozenset(self.types.keys()) != frozenset(other.types.keys()):
    exit(False)
ret = all(self.types[s] == other.types[s] for s in self.types)
exit(ret)
