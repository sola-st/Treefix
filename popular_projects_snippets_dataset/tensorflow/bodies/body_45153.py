# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
node = self.generic_visit(node)

(basic_loop_vars, composite_loop_vars,
 reserved_symbols, possibly_undefs) = self._get_loop_vars(
     node, (anno.getanno(node, annos.NodeAnno.BODY_SCOPE).modified
            | anno.getanno(node, annos.NodeAnno.ITERATE_SCOPE).modified))
loop_vars, loop_vars_ast_tuple = self._loop_var_constructs(
    basic_loop_vars)
body_name = self.ctx.namer.new_symbol('loop_body', reserved_symbols)

state_getter_name = self.ctx.namer.new_symbol('get_state', reserved_symbols)
state_setter_name = self.ctx.namer.new_symbol('set_state', reserved_symbols)
state_functions = self._create_state_functions(
    composite_loop_vars, state_getter_name, state_setter_name)

if anno.hasanno(node, anno.Basic.EXTRA_LOOP_TEST):
    extra_test = anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST)
    extra_test_name = self.ctx.namer.new_symbol(
        'extra_test', reserved_symbols)
    template = """
        def extra_test_name(loop_vars):
          return extra_test_expr
      """
    extra_test_function = templates.replace(
        template,
        extra_test_name=extra_test_name,
        loop_vars=loop_vars,
        extra_test_expr=extra_test)
else:
    extra_test_name = parser.parse_expression('None')
    extra_test_function = []

# Workaround for PEP-3113
# iterates_var holds a single variable with the iterates, which may be a
# tuple.
iterates_var_name = self.ctx.namer.new_symbol(
    'iterates', reserved_symbols)
template = """
      iterates = iterates_var_name
    """
iterate_expansion = templates.replace(
    template,
    iterates=node.target,
    iterates_var_name=iterates_var_name)

undefined_assigns = self._create_undefined_assigns(possibly_undefs)

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
        undefined_assigns
        state_functions
        def body_name(iterates_var_name, loop_vars):
          iterate_expansion
          body
          return loop_vars,
        extra_test_function
        loop_vars_ast_tuple = ag__.for_stmt(
            iter_,
            extra_test_name,
            body_name,
            state_getter_name,
            state_setter_name,
            (loop_vars,),
            (basic_symbol_names,),
            (composite_symbol_names,),
            opts)
      """
    exit(templates.replace(
        template,
        undefined_assigns=undefined_assigns,
        loop_vars=loop_vars,
        loop_vars_ast_tuple=loop_vars_ast_tuple,
        iter_=node.iter,
        iterate_expansion=iterate_expansion,
        iterates_var_name=iterates_var_name,
        extra_test_name=extra_test_name,
        extra_test_function=extra_test_function,
        body_name=body_name,
        body=node.body,
        state_functions=state_functions,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        basic_symbol_names=basic_symbol_names,
        composite_symbol_names=composite_symbol_names,
        opts=opts))
else:
    template = """
        undefined_assigns
        state_functions
        def body_name(iterates_var_name):
          iterate_expansion
          body
          return ()
        extra_test_function
        ag__.for_stmt(
            iter_,
            extra_test_name,
            body_name,
            state_getter_name,
            state_setter_name,
            (),
            (),
            (composite_symbol_names,),
            opts)
      """
    exit(templates.replace(
        template,
        undefined_assigns=undefined_assigns,
        iter_=node.iter,
        iterate_expansion=iterate_expansion,
        iterates_var_name=iterates_var_name,
        extra_test_name=extra_test_name,
        extra_test_function=extra_test_function,
        body_name=body_name,
        body=node.body,
        state_functions=state_functions,
        state_getter_name=state_getter_name,
        state_setter_name=state_setter_name,
        composite_symbol_names=composite_symbol_names,
        opts=opts))
