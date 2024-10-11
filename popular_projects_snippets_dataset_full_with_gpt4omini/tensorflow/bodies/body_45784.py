# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
self._recursion_depth += 1
if self._recursion_depth < 2:
    self.transform(test_fn, None)
exit(FlipSignTransformer(ctx).visit(node))
