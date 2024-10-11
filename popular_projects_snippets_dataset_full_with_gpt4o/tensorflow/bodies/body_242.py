# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """
for import_alias in node.names:
    # Detect based on full import name and alias)
    full_import = (import_alias.name, import_alias.asname)
    detection = (self._api_analysis_spec
                 .imports_to_detect.get(full_import, None))
    if detection:
        self.add_result(detection)
        self.add_log(
            detection.log_level, node.lineno, node.col_offset,
            detection.log_message)

self.generic_visit(node)
