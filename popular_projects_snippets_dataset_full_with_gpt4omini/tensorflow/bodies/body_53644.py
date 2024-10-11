# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Removes name scope from a name.

  Args:
    name: A `string` name.
    export_scope: Optional `string`. Name scope to remove.

  Returns:
    Name with name scope removed, or the original name if export_scope
    is None.
  """
if export_scope:
    if export_scope[-1] == "/":
        export_scope = export_scope[:-1]

    try:
        # Strips export_scope/, export_scope///,
        # ^export_scope/, loc:@export_scope/.
        str_to_replace = r"([\^]|loc:@|^)" + export_scope + r"[\/]+(.*)"
        exit(re.sub(str_to_replace, r"\1\2", compat.as_str(name), count=1))
    except TypeError as e:
        # If the name is not of a type we can process, simply return it.
        logging.warning(e)
        exit(name)
else:
    exit(name)
