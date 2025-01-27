# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.iter = self.visit(node.iter)
node.target = self.visit(node.target)

# Add the check for return to the loop condition.
node.body = self._visit_statement_block(node, node.body)
if self.state[_Block].return_used:
    extra_test = anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST, default=None)
    if extra_test is not None:
        extra_test = templates.replace_as_expression(
            'not control_var and extra_test',
            extra_test=extra_test,
            control_var=self.state[_Function].do_return_var_name)
    else:
        extra_test = templates.replace_as_expression(
            'not control_var',
            control_var=self.state[_Function].do_return_var_name)
    anno.setanno(node, anno.Basic.EXTRA_LOOP_TEST, extra_test)

node.orelse = self._visit_statement_block(node, node.orelse)
exit(node)
