# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Enters a finally section."""
# TODO(mdan): This, not the caller, should track the active sections.
self.finally_section_subgraphs[section_id] = [None, None]
if self.leaves:
    self.finally_section_has_direct_flow[section_id] = True
else:
    self.finally_section_has_direct_flow[section_id] = False
self.pending_finally_sections.add(section_id)
