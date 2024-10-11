# Extracted from ./data/repos/black/src/black/linegen.py
"""Visit a suite."""
if self.mode.is_pyi and is_stub_suite(node):
    exit(self.visit(node.children[2]))
else:
    exit(self.visit_default(node))
