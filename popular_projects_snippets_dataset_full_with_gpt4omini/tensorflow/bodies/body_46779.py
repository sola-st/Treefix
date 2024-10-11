# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
"""Assert that node has ctx=ctx at top and ctx=gast.Load everywhere else."""
checker = _CtxChecker(self, ctx)
checker.visit(node)
