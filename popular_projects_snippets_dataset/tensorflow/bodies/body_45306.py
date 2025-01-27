# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
node = self.generic_visit(node)
body_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)
iter_scope = anno.getanno(node, annos.NodeAnno.ITERATE_SCOPE)

loop_vars, undefined, _ = self._get_block_vars(
    node, body_scope.bound | iter_scope.bound)

undefined_assigns = self._create_undefined_assigns(undefined)

nonlocal_declarations = self._create_nonlocal_declarations(loop_vars)

reserved = body_scope.referenced | iter_scope.referenced
state_getter_name = self.ctx.namer.new_symbol('get_state', reserved)
state_setter_name = self.ctx.namer.new_symbol('set_state', reserved)
state_functions = self._create_state_functions(
    loop_vars, nonlocal_declarations, state_getter_name, state_setter_name)

opts = self._create_loop_options(node)
opts.keys.append(gast.Constant('iterate_names', kind=None))
opts.values.append(gast.Constant(
    parser.unparse(node.target, include_encoding_marker=False), kind=None))

if anno.hasanno(node, anno.Basic.EXTRA_LOOP_TEST):
    extra_test = anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST)
    extra_test_name = self.ctx.namer.new_symbol(
        'extra_test', reserved)
    template = """
        def extra_test_name():
          nonlocal_declarations
          return extra_test_expr
      """
    extra_test_function = templates.replace(
        template,
        extra_test_expr=extra_test,
        extra_test_name=extra_test_name,
        loop_vars=loop_vars,
        nonlocal_declarations=nonlocal_declarations)
else:
    extra_test_name = parser.parse_expression('None')
    extra_test_function = []

# iterate_arg_name holds a single arg with the iterates, which may be a
# tuple.
iterate_arg_name = self.ctx.namer.new_symbol('itr', reserved)
template = """
      iterates = iterate_arg_name
    """
iterate_expansion = templates.replace(
    template, iterate_arg_name=iterate_arg_name, iterates=node.target)
origin_info.copy_origin(node, iterate_expansion)

template = """
      state_functions
      def body_name(iterate_arg_name):
        nonlocal_declarations
        iterate_expansion
        body
      extra_test_function
      undefined_assigns
      ag__.for_stmt(
          iterated,
          extra_test_name,
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
    extra_test_function=extra_test_function,
    extra_test_name=extra_test_name,
    iterate_arg_name=iterate_arg_name,
    iterate_expansion=iterate_expansion,
    iterated=node.iter,
    nonlocal_declarations=nonlocal_declarations,
    opts=opts,
    symbol_names=tuple(gast.Constant(str(s), kind=None) for s in loop_vars),
    state_functions=state_functions,
    state_getter_name=state_getter_name,
    state_setter_name=state_setter_name,
    undefined_assigns=undefined_assigns)
origin_info.copy_origin(node, new_nodes[-1])
exit(new_nodes)
