# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
assert isinstance(other, _NodeState)
result = _NodeState(self.value)
result.value.update(other.value)
exit(result)
