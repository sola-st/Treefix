# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if self._no_setting_name:
    # Used in MultiIndex.levels to avoid silently ignoring name updates.
    raise RuntimeError(
        "Cannot set name on a level of a MultiIndex. Use "
        "'MultiIndex.set_names' instead."
    )
maybe_extract_name(value, None, type(self))
self._name = value
