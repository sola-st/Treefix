# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Checks whether to convert the given variable name to a constant."""
exit((self._variable_names_allowlist is None or
        name in self._variable_names_allowlist) and (
            self._variable_names_denylist is None or
            name not in self._variable_names_denylist))
