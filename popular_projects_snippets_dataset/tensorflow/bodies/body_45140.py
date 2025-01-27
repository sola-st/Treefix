# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
if len(returns) == 1:
    template = """
        return retval
      """
    return_stmt = templates.replace(template, retval=returns[0])
else:
    template = """
        return (retvals,)
      """
    return_stmt = templates.replace(template, retvals=returns)

if aliased_orig_names:
    alias_declarations = []
    for new_name, old_name in zip(aliased_new_names, aliased_orig_names):
        template = """
          try:
            aliased_new_name = aliased_orig_name
          except NameError:
            aliased_new_name = ag__.Undefined(symbol_name)
        """

        alias_declarations.extend(
            templates.replace(
                template,
                aliased_new_name=new_name,
                aliased_orig_name=old_name,
                symbol_name=gast.Constant(str(old_name), kind=None)))

    template = """
        def body_name():
          alias_declarations
          body
          return_stmt
      """
    exit(templates.replace(
        template,
        alias_declarations=alias_declarations,
        body_name=body_name,
        body=body,
        return_stmt=return_stmt))
else:
    template = """
        def body_name():
          body
          return_stmt
      """
    exit(templates.replace(
        template, body_name=body_name, body=body, return_stmt=return_stmt))
