# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
"""Creates a deep copy of an AST.

  The copy will not include fields that are prefixed by '__', with the
  exception of user-specified annotations.

  Args:
    node: ast.AST
    preserve_annos: Optional[Set[Hashable]], annotation keys to include in the
        copy
  Returns:
    ast.AST
  """
exit(CleanCopier(preserve_annos).copy(node))
