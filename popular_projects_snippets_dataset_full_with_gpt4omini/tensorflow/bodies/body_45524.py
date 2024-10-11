# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions.py
with self.state[_Function] as fn_scope:
    scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)

    function_context_name = self.ctx.namer.new_symbol('fscope',
                                                      scope.referenced)
    fn_scope.context_name = function_context_name
    anno.setanno(node, 'function_context_name', function_context_name)

    node = self.generic_visit(node)

    if fn_scope.level <= 2:
        # Top-level functions lose their decorator because the conversion is
        # always just-in-time and by the time it happens the decorators are
        # already set to be applied.
        node.decorator_list = []
    else:
        # TODO(mdan): Fix the tests so that we can always add this decorator.
        # Inner functions are converted already, so we insert a decorator to
        # prevent double conversion. Double conversion would work too, but this
        # saves the overhead.
        node.decorator_list.append(
            parser.parse_expression('ag__.autograph_artifact'))

    docstring_node = None
    if node.body:
        first_statement = node.body[0]
        if (isinstance(first_statement, gast.Expr) and
            isinstance(first_statement.value, gast.Constant)):
            docstring_node = first_statement
            node.body = node.body[1:]

    template = """
        with ag__.FunctionScope(
            function_name, context_name, options) as function_context:
          body
      """
    wrapped_body = templates.replace(
        template,
        function_name=gast.Constant(node.name, kind=None),
        context_name=gast.Constant(function_context_name, kind=None),
        options=self._function_scope_options(fn_scope).to_ast(),
        function_context=function_context_name,
        body=node.body)

    if docstring_node is not None:
        wrapped_body = [docstring_node] + wrapped_body

    node.body = wrapped_body

    exit(node)
