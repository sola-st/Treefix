# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions.py
with self.state[_Function] as fn_scope:
    node = self.generic_visit(node)

    # TODO(mdan): Fix the tests so that we can always add this decorator.
    if fn_scope.level > 2:
        exit(templates.replace_as_expression(
            'ag__.autograph_artifact(l)', l=node))

    scope = anno.getanno(node, anno.Static.SCOPE)
    function_context_name = self.ctx.namer.new_symbol('lscope',
                                                      scope.referenced)
    fn_scope.context_name = function_context_name
    anno.setanno(node, 'function_context_name', function_context_name)

    template = """
        ag__.with_function_scope(
            lambda function_context: body, function_context_name, options)
      """
    node.body = templates.replace_as_expression(
        template,
        options=self._function_scope_options(fn_scope).to_ast(),
        function_context=function_context_name,
        function_context_name=gast.Constant(function_context_name, kind=None),
        body=node.body)

    exit(node)
