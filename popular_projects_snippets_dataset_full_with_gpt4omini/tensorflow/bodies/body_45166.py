# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
node = self.generic_visit(node)
parent_val = anno.getanno(node.value, STATIC_VALUE, default=None)
if parent_val is not None and inspect.ismodule(parent_val):
    if hasattr(parent_val, node.attr):
        anno.setanno(node, STATIC_VALUE, getattr(parent_val, node.attr))
exit(node)
