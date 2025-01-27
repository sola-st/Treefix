# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
if results is not None:
    template = """
        results = ag__.if_stmt(test, body_name, orelse_name,
                               state_getter_name, state_setter_name,
                               (basic_symbol_names,),
                               (composite_symbol_names,))
      """
    exit(templates.replace(
        template,
        test=test,
        results=results,
        body_name=body_name,
        orelse_name=orelse_name,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        basic_symbol_names=basic_symbol_names,
        composite_symbol_names=composite_symbol_names))
else:
    template = """
        ag__.if_stmt(test, body_name, orelse_name, getter_name, setter_name,
                     (basic_symbol_names,), (composite_symbol_names,))
      """
    exit(templates.replace(
        template,
        test=test,
        body_name=body_name,
        orelse_name=orelse_name,
        getter_name=state_getter_name,
        setter_name=state_setter_name,
        basic_symbol_names=basic_symbol_names,
        composite_symbol_names=composite_symbol_names))
