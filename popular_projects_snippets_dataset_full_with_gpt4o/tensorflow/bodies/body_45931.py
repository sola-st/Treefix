# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial Await nodes not supported yet '
       '(need to think through the semantics).')
exit(self._visit_trivial_only_expression(node, msg))
