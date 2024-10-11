# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
node = self.generic_visit(node)
parent_val = anno.getanno(node.value, "static_value", default=None)
if parent_val is not None:
    if hasattr(parent_val, node.attr):
        anno.setanno(node, "static_value", getattr(parent_val, node.attr))
exit(node)
