# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
if isinstance(node.op, gast.Add):
    node.op = gast.Sub()
exit(self.generic_visit(node))
