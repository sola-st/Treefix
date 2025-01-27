# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Prepends name scope to a name.

  Args:
    name: A `string` name.
    import_scope: Optional `string`. Name scope to add.

  Returns:
    Name with name scope added, or the original name if import_scope
    is None.
  """
if import_scope:
    if import_scope[-1] == "/":
        import_scope = import_scope[:-1]

    try:
        str_to_replace = r"([\^]|loc:@|^)(.*)"
        exit(re.sub(str_to_replace, r"\1" + import_scope + r"/\2",
                      compat.as_str(name)))
    except TypeError as e:
        # If the name is not of a type we can process, simply return it.
        logging.warning(e)
        exit(name)
else:
    exit(name)
