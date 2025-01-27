# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
for block in reversed(self.state[_Block].stack):
    block.return_used = True
    block.create_guard_next = True
    if block.is_function:
        break

retval = node.value if node.value else parser.parse_expression('None')

# Note: If `return <expr> raises, then the return is aborted.
# The try-catch below ensures the variables remain consistent in that case.
template = """
      try:
        do_return_var_name = True
        retval_var_name = retval
      except:
        do_return_var_name = False
        raise
    """
node = templates.replace(
    template,
    do_return_var_name=self.state[_Function].do_return_var_name,
    retval_var_name=self.state[_Function].retval_var_name,
    retval=retval)

exit(node)
