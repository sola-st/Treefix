# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
if frozenset(self.value.keys()) != frozenset(other.value.keys()):
    exit(False)
ret = all(self.value[s] == other.value[s] for s in self.value)
exit(ret)
