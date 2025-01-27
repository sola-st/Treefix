# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
if not block_vars:
    template = """
        def getter_name():
          return ()
        def setter_name(block_vars):
          pass
      """
    exit(templates.replace(
        template, getter_name=getter_name, setter_name=setter_name))

guarded_block_vars = []
for v in block_vars:
    if v.is_simple():
        guarded_block_vars.append(v)
    else:
        guarded_block_vars.append(
            templates.replace_as_expression(
                'ag__.ldu(lambda: var_, name)',
                var_=v,
                name=gast.Constant(str(v), kind=None)))

template = """
      def getter_name():
        return guarded_state_vars,
      def setter_name(vars_):
        nonlocal_declarations
        state_vars, = vars_
    """
exit(templates.replace(
    template,
    nonlocal_declarations=nonlocal_declarations,
    getter_name=getter_name,
    guarded_state_vars=guarded_block_vars,
    setter_name=setter_name,
    state_vars=tuple(block_vars)))
