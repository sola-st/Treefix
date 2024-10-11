# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Exits a finally section."""
assert section_id not in self.pending_finally_sections, 'Empty finally?'
self.finally_section_subgraphs[section_id][1] = self.leaves
# If the guard can only be reached by a jump, then it will not flow
# into the statement that follows it.
if not self.finally_section_has_direct_flow[section_id]:
    self.leaves = set()
del self.finally_section_has_direct_flow[section_id]
