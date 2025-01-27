# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
if hasattr(ast, "NameConstant"):
    exit(isinstance(node, ast.NameConstant) and node.value is True)
else:
    exit(isinstance(node, ast.Name) and node.id == "True")
