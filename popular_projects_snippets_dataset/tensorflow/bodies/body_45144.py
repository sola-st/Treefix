# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py

if composites:
    composite_tuple = tuple(composites)

    template = """
        def state_getter_name():
          return composite_tuple,
        def state_setter_name(vals):
          composite_tuple, = vals
      """
    node = templates.replace(
        template,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        composite_tuple=composite_tuple)
else:
    template = """
        def state_getter_name():
          return ()
        def state_setter_name(_):
          pass
        """
    node = templates.replace(
        template,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name)

exit(node)
