# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.test = self.visit(node.test)

# Add the check for return to the loop condition.
node.body = self._visit_statement_block(node, node.body)
if self.state[_Block].return_used:
    node.test = templates.replace_as_expression(
        'not control_var and test',
        test=node.test,
        control_var=self.state[_Function].do_return_var_name)

node.orelse = self._visit_statement_block(node, node.orelse)
exit(node)
