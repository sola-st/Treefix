# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
if not isinstance(api_change_spec, APIChangeSpec):
    raise TypeError("Must pass APIChangeSpec to ASTCodeUpgrader, got %s" %
                    type(api_change_spec))
self._api_change_spec = api_change_spec
