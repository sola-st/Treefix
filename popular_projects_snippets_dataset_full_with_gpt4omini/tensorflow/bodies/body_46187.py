# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
entered_function = False
if isinstance(node, gast.FunctionDef):
    entered_function = True
    self._function_stack.append(_Function(node.name))

self._attach_origin_info(node)
self.generic_visit(node)

if entered_function:
    self._function_stack.pop()
