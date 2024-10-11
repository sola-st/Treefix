# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
node = self.generic_visit(node)
body_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)

loop_vars, undefined, _ = self._get_block_vars(node, body_scope.bound)

undefined_assigns = self._create_undefined_assigns(undefined)

nonlocal_declarations = self._create_nonlocal_declarations(loop_vars)

reserved = body_scope.referenced
state_getter_name = self.ctx.namer.new_symbol('get_state', reserved)
state_setter_name = self.ctx.namer.new_symbol('set_state', reserved)
state_functions = self._create_state_functions(
    loop_vars, nonlocal_declarations, state_getter_name, state_setter_name)

opts = self._create_loop_options(node)

template = """
      state_functions
      def body_name():
        nonlocal_declarations
        body
      def test_name():
        return test
      undefined_assigns
      ag__.while_stmt(
          test_name,
          body_name,
          state_getter_name,
          state_setter_name,
          (symbol_names,),
          opts)
    """
new_nodes = templates.replace(
    template,
    body=node.body,
    body_name=self.ctx.namer.new_symbol('loop_body', reserved),
    nonlocal_declarations=nonlocal_declarations,
    opts=opts,
    state_functions=state_functions,
    state_getter_name=state_getter_name,
    state_setter_name=state_setter_name,
    symbol_names=tuple(gast.Constant(str(s), kind=None) for s in loop_vars),
    test=node.test,
    test_name=self.ctx.namer.new_symbol('loop_test', reserved),
    undefined_assigns=undefined_assigns)
origin_info.copy_origin(node, new_nodes[-1])
exit(new_nodes)
