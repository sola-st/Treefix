# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
if self.state[_Continue].used:
    block = self.state[_Block]
    should_wrap_current = block.create_guard_current
    # After processing propagate whether to guard the next statement
    block.create_guard_current = block.create_guard_next
    block.create_guard_next = False
    if should_wrap_current:
        template = """
          if not var_name:
            original_node
        """
        cond, = templates.replace(
            template,
            var_name=self.state[_Continue].control_var_name,
            original_node=node)
        exit((cond, cond.body))
exit((node, None))
