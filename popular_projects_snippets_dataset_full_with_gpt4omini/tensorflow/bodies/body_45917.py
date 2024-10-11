# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial Assert nodes not supported yet '
       '(need to avoid computing the test when assertions are off, and '
       'avoid computing the irritant when the assertion does not fire).')
exit(self._visit_trivial_only_statement(node, msg))
