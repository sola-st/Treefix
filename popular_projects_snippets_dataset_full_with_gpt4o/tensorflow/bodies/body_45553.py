# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
with self.state[_Function] as fn:
    with self.state[_Block] as block:
        block.is_function = True

        scope = anno.getanno(node, NodeAnno.BODY_SCOPE)
        do_return_var_name = self.ctx.namer.new_symbol('do_return',
                                                       scope.referenced)
        retval_var_name = self.ctx.namer.new_symbol('retval_', scope.referenced)
        fn.do_return_var_name = do_return_var_name
        fn.retval_var_name = retval_var_name

        node.body = self._visit_statement_block(node, node.body)

        if block.return_used:

            if self.allow_missing_return:
                # The function would have a single `with` node that wraps the
                # entire body. If the function had a docstring, the body has two
                # nodes, with the `with` as the second node.
                wrapper_node = node.body[-1]
                assert isinstance(wrapper_node, gast.With), (
                    'This transformer requires the functions converter.')

                template = """
              do_return_var_name = False
              retval_var_name = ag__.UndefinedReturnValue()
              body
              return function_context.ret(retval_var_name, do_return_var_name)
            """

                wrapper_node.body = templates.replace(
                    template,
                    body=wrapper_node.body,
                    do_return_var_name=do_return_var_name,
                    function_context=anno.getanno(node, 'function_context_name'),
                    retval_var_name=retval_var_name)
            else:
                template = """
              body
              return retval_var_name
            """
                node.body = templates.replace(
                    template,
                    body=node.body,
                    do_return_var_name=do_return_var_name,
                    retval_var_name=retval_var_name)

exit(node)
