# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
if self._arg_accumulator:
    self._argspec.append(
        gast.Tuple(elts=self._arg_accumulator, ctx=gast.Load()))
    self._arg_accumulator = []
