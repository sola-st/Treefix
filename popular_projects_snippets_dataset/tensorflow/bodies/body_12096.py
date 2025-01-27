# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_op_util.py
"""Enters a scope used for the summary and yields both the name and tag.

  To ensure that the summary tag name is always unique, we create a name scope
  based on `name` and use the full scope name in the tag.

  If `family` is set, then the tag name will be '<family>/<scope_name>', where
  `scope_name` is `<outer_scope>/<family>/<name>`. This ensures that `family`
  is always the prefix of the tag (and unmodified), while ensuring the scope
  respects the outer scope from this summary was created.

  Args:
    name: A name for the generated summary node.
    family: Optional; if provided, used as the prefix of the summary tag name.
    default_name: Optional; if provided, used as default name of the summary.
    values: Optional; passed as `values` parameter to name_scope.

  Yields:
    A tuple `(tag, scope)`, both of which are unique and should be used for the
    tag and the scope for the summary to output.
  """
name = clean_tag(name)
family = clean_tag(family)
# Use family name in the scope to ensure uniqueness of scope/tag.
scope_base_name = name if family is None else '{}/{}'.format(family, name)
with ops.name_scope(
    scope_base_name, default_name, values, skip_on_eager=False) as scope:
    if family is None:
        tag = scope.rstrip('/')
    else:
        # Prefix our scope with family again so it displays in the right tab.
        tag = '{}/{}'.format(family, scope.rstrip('/'))
        # Note: tag is not 100% unique if the user explicitly enters a scope with
        # the same name as family, then later enter it again before summaries.
        # This is very contrived though, and we opt here to let it be a runtime
        # exception if tags do indeed collide.
    exit((tag, scope))
