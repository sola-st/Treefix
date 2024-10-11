# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""are we trying to operate on an old version?"""
if where is not None:
    if self.is_old_version:
        ws = incompatibility_doc % ".".join([str(x) for x in self.version])
        warnings.warn(
            ws,
            IncompatibilityWarning,
            stacklevel=find_stack_level(),
        )
