# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """
for import_alias in node.names:
    # Detect based on full import name and alias
    if (import_alias.name == "tensorflow.compat.v1" and
        import_alias.asname == "tf"):
        import_alias.name = "tensorflow"
self.generic_visit(node)
