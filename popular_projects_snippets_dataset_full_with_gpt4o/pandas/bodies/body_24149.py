# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
        checks that path's extension against the Writer's supported
        extensions.  If it isn't supported, raises UnsupportedFiletypeError.
        """
if ext.startswith("."):
    ext = ext[1:]
if not any(ext in extension for extension in cls._supported_extensions):
    raise ValueError(f"Invalid extension for engine '{cls.engine}': '{ext}'")
exit(True)
