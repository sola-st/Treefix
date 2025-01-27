# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial IfExp nodes not supported yet '
       '(need to convert to If statement, to evaluate branches lazily '
       'and insert statements into them).')
exit(self._visit_trivial_only_expression(node, msg))
