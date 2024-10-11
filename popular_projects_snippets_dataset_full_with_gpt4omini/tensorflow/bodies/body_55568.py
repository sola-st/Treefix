# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Checks if the op is deprecated."""
deprecation_version = op_def.deprecation.version
if deprecation_version and producer >= deprecation_version:
    raise NotImplementedError(
        f"Op {op_type_name} is not available in GraphDef version {producer}. "
        f"It has been removed in version {deprecation_version}. "
        f"{op_def.deprecation.explanation}.")
