# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate a While node."""

test = self.generate_Compare()
body = self.sample_node_list(
    low=1, high=N_CONTROLFLOW_STATEMENTS, generator=self.generate_statement)
orelse = []  # not generating else statements

node = gast.While(test, body, orelse)
exit(node)
