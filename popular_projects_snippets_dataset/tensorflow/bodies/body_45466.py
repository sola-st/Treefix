# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
self.state[_Break].enter()
self.state[_Break].control_var_name = break_var
nodes = self.visit_block(nodes)
break_used = self.state[_Break].used
self.state[_Break].exit()
exit((nodes, break_used))
