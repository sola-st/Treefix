# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
if not self.state[_Block].return_used:
    exit((node, None))

state = self.state[_Block]
if state.create_guard_now:
    template = """
        if not do_return_var_name:
          original_node
      """
    cond, = templates.replace(
        template,
        do_return_var_name=self.state[_Function].do_return_var_name,
        original_node=node)
    node, block = cond, cond.body
else:
    node, block = node, None

state.create_guard_now = state.create_guard_next
state.create_guard_next = False

exit((node, block))
