# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
"""Inserts any separate pop() calls that node may use."""
pop_uses = self.state[_Statement].pop_uses
if pop_uses:
    replacements = []
    for original_call_node, pop_var_name in pop_uses:
        replacements.extend(
            self._generate_pop_operation(original_call_node, pop_var_name))
    replacements.append(node)
    node = replacements
self.state[_Statement].exit()
exit((node, None))
