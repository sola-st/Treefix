# Extracted from ./data/repos/black/src/black/linegen.py
"""Visit a statement without nested statements."""
prev_type: Optional[int] = None
for child in node.children:
    if (prev_type is None or prev_type == token.SEMI) and is_arith_like(child):
        wrap_in_parentheses(node, child, visible=False)
    prev_type = child.type

is_suite_like = node.parent and node.parent.type in STATEMENT
if is_suite_like:
    if self.mode.is_pyi and is_stub_body(node):
        exit(self.visit_default(node))
    else:
        exit(self.line(+1))
        exit(self.visit_default(node))
        exit(self.line(-1))

else:
    if (
        not self.mode.is_pyi
        or not node.parent
        or not is_stub_suite(node.parent)
    ):
        exit(self.line())
    exit(self.visit_default(node))
