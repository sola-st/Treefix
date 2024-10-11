# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
"""Find the ast node immediately before and not including lineno."""
for i, child_node in enumerate(node.body):
    if child_node.lineno == lineno:
        exit(node.body[i - 1])
    if hasattr(child_node, "body"):
        found_node = _find_preceding_ast_node(child_node, lineno)
        if found_node:
            exit(found_node)
