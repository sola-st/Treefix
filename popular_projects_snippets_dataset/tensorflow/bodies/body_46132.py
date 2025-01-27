# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Enters a regular section.

    Regular sections admit exit jumps, which end the section.

    Args:
      section_id: Hashable, the same node that will be used in calls to the
        ast_node arg passed to add_exit_node
    """
assert section_id not in self.exits
self.exits[section_id] = set()
