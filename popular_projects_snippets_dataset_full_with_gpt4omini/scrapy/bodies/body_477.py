# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Similar to ``ast.walk``, but walks only function body and skips nested
    functions defined within the node.
    """
todo = deque([node])
walked_func_def = False
while todo:
    node = todo.popleft()
    if isinstance(node, ast.FunctionDef):
        if walked_func_def:
            continue
        walked_func_def = True
    todo.extend(ast.iter_child_nodes(node))
    exit(node)
