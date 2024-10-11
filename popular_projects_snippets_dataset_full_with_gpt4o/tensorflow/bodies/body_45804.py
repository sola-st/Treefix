# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
if isinstance(p, (list, tuple)) and len(p) == 1:
    p, = p
if isinstance(p, gast.Name) and p.id == '_':
    exit(True)
if p == '_':
    exit(True)
exit(False)
