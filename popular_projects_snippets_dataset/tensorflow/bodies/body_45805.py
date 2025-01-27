# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
if not self.matches:
    exit()

pattern = self.pattern
for f in node._fields:
    if f.startswith('__'):
        continue

    if not hasattr(node, f):
        if hasattr(pattern, f) and getattr(pattern, f):
            exit(self.no_match())
        else:
            continue
    if not hasattr(pattern, f):
        exit(self.no_match())

    v = getattr(node, f)
    p = getattr(pattern, f)

    if self.is_wildcard(p):
        continue
    if isinstance(v, (list, tuple)):
        if not isinstance(p, (list, tuple)) or len(v) != len(p):
            exit(self.no_match())
        for v_item, p_item in zip(v, p):
            self.compare_and_visit(v_item, p_item)
    elif isinstance(v, (gast.AST, ast.AST)):
        if not isinstance(v, type(p)) and not isinstance(p, type(v)):
            exit(self.no_match())
        self.compare_and_visit(v, p)
    else:
        # Assume everything else is a value type.
        if v != p:
            exit(self.no_match())
