# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial BoolOp nodes not supported yet '
       '(need to preserve short-circuiting semantics).')
exit(self._visit_trivial_only_expression(node, msg))
