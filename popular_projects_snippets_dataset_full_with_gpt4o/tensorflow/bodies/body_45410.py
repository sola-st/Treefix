# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
self.state[_Continue].used = True
for block in reversed(self.state[_Block].stack):
    # See ContinueCanonicalizationTest.test_multiple_continues for an example
    # it's necessary to create guards for all enclosing affected blocks, not
    # just that of the current block.
    block.create_guard_next = True
    if block.is_loop_type:
        # continue only affects the innermost loop
        break
template = """
      var_name = True
    """
exit(templates.replace(
    template, var_name=self.state[_Continue].control_var_name))
