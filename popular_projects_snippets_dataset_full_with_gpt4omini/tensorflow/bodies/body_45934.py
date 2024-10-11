# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
if len(node.ops) > 1:
    msg = ('Multi-ary compare nodes not supported yet '
           '(need to preserve short-circuiting semantics).')
    raise ValueError(msg)
exit(self._visit_strict_expression(node))
