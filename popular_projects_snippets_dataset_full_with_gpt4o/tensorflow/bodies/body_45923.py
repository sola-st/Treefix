# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('Nontrivial Lambda nodes not supported '
       '(cannot insert statements into lambda bodies).')
exit(self._visit_trivial_only_expression(node, msg))
