# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
self._stack.append(node)
super(_PastaEditVisitor, self).visit(node)
self._stack.pop()
