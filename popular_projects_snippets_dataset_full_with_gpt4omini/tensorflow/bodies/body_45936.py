# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial Repr nodes not supported yet '
       '(need to research their syntax and semantics).')
exit(self._visit_trivial_only_expression(node, msg))
