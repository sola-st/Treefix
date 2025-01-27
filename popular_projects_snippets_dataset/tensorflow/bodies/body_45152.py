# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
node = self.generic_visit(node)

(basic_loop_vars, composite_loop_vars, reserved_symbols,
 possibly_undefs) = self._get_loop_vars(
     node,
     anno.getanno(node, annos.NodeAnno.BODY_SCOPE).modified)
loop_vars, loop_vars_ast_tuple = self._loop_var_constructs(
    basic_loop_vars)

state_getter_name = self.ctx.namer.new_symbol('get_state', reserved_symbols)
state_setter_name = self.ctx.namer.new_symbol('set_state', reserved_symbols)
state_functions = self._create_state_functions(
    composite_loop_vars, state_getter_name, state_setter_name)

basic_symbol_names = tuple(
    gast.Constant(str(symbol), kind=None) for symbol in basic_loop_vars)
composite_symbol_names = tuple(
    gast.Constant(str(symbol), kind=None) for symbol in composite_loop_vars)

opts = self._create_loop_options(node)

# TODO(mdan): Use a single template.
# If the body and test functions took a single tuple for loop_vars, instead
# of *loop_vars, then a single template could be used.
if loop_vars:
    template = """
        state_functions
        def body_name(loop_vars):
          body
          return loop_vars,
        def test_name(loop_vars):
          return test
        loop_vars_ast_tuple = ag__.while_stmt(
            test_name,
            body_name,
            state_getter_name,
            state_setter_name,
            (loop_vars,),
            (basic_symbol_names,),
            (composite_symbol_names,),
            opts)
      """
    node = templates.replace(
        template,
        loop_vars=loop_vars,
        loop_vars_ast_tuple=loop_vars_ast_tuple,
        test_name=self.ctx.namer.new_symbol('loop_test', reserved_symbols),
        test=node.test,
        body_name=self.ctx.namer.new_symbol('loop_body', reserved_symbols),
        body=node.body,
        state_functions=state_functions,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        basic_symbol_names=basic_symbol_names,
        composite_symbol_names=composite_symbol_names,
        opts=opts)
else:
    template = """
        state_functions
        def body_name():
          body
          return ()
        def test_name():
          return test
        ag__.while_stmt(
            test_name,
            body_name,
            state_getter_name,
            state_setter_name,
            (),
            (),
            (composite_symbol_names,),
            opts)
      """
    node = templates.replace(
        template,
        test_name=self.ctx.namer.new_symbol('loop_test', reserved_symbols),
        test=node.test,
        body_name=self.ctx.namer.new_symbol('loop_body', reserved_symbols),
        body=node.body,
        state_functions=state_functions,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        composite_symbol_names=composite_symbol_names,
        opts=opts)

undefined_assigns = self._create_undefined_assigns(possibly_undefs)
exit(undefined_assigns + node)
