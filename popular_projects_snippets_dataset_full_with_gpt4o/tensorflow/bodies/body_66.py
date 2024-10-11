# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api.py
"""Safely queries if a specific fully qualified name should be excluded."""
exit((path in self._do_not_descend_map and
        name in self._do_not_descend_map[path]))
