# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
if key not in self._value:
    self._value[key] = _StateStack(key)
exit(self._value[key])
