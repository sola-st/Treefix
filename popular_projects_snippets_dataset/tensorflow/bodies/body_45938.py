# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial JoinedStr nodes not supported yet '
       '(need to unit-test them in Python 2).')
exit(self._visit_trivial_only_expression(node, msg))
