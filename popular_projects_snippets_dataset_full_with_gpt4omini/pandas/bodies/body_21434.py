# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/extension_types.py
if isinstance(other, pyarrow.BaseExtensionType):
    exit((
        type(self) == type(other)
        and self.subtype == other.subtype
        and self.closed == other.closed
    ))
else:
    exit(NotImplemented)
