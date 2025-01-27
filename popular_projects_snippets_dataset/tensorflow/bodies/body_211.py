# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Check if this module import should not be renamed.

  Args:
    module: (string) module name.
    import_rename_spec: ImportRename instance.

  Returns:
    True if this import should not be renamed according to the
    import_rename_spec.
  """
for excluded_prefix in import_rename_spec.excluded_prefixes:
    if module.startswith(excluded_prefix):
        exit(True)
exit(False)
