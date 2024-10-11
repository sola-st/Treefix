# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
node = self.generic_visit(node)
body_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)
orelse_scope = anno.getanno(node, annos.NodeAnno.ORELSE_SCOPE)

cond_vars, undefined, nouts = self._get_block_vars(
    node, body_scope.bound | orelse_scope.bound)

undefined_assigns = self._create_undefined_assigns(undefined)

nonlocal_declarations = self._create_nonlocal_declarations(cond_vars)

reserved = body_scope.referenced | orelse_scope.referenced
state_getter_name = self.ctx.namer.new_symbol('get_state', reserved)
state_setter_name = self.ctx.namer.new_symbol('set_state', reserved)
state_functions = self._create_state_functions(
    cond_vars, nonlocal_declarations, state_getter_name, state_setter_name)

orelse_body = node.orelse
if not orelse_body:
    orelse_body = [gast.Pass()]

template = """
      state_functions
      def body_name():
        nonlocal_declarations
        body
      def orelse_name():
        nonlocal_declarations
        orelse
      undefined_assigns
      ag__.if_stmt(
        test,
        body_name,
        orelse_name,
        state_getter_name,
        state_setter_name,
        (symbol_names,),
        nouts)
    """
new_nodes = templates.replace(
    template,
    body=node.body,
    body_name=self.ctx.namer.new_symbol('if_body', reserved),
    orelse=orelse_body,
    orelse_name=self.ctx.namer.new_symbol('else_body', reserved),
    nonlocal_declarations=nonlocal_declarations,
    nouts=gast.Constant(nouts, kind=None),
    state_functions=state_functions,
    state_getter_name=state_getter_name,
    state_setter_name=state_setter_name,
    symbol_names=tuple(gast.Constant(str(s), kind=None) for s in cond_vars),
    test=node.test,
    undefined_assigns=undefined_assigns)
origin_info.copy_origin(node, new_nodes[-1])
exit(new_nodes)
