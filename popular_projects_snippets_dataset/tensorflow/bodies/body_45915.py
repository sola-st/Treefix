# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial AsyncWith nodes not supported yet '
       '(need to think through the semantics).')
exit(self._visit_trivial_only_statement(node, msg))
