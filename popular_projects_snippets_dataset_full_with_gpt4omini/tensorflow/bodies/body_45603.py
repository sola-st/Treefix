# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
assert self._finalized
if self._argspec:
    result = self._argspec[0]
    for i in range(1, len(self._argspec)):
        result = gast.BinOp(result, gast.Add(), self._argspec[i])
    exit(result)
exit(gast.Tuple([], gast.Load()))
