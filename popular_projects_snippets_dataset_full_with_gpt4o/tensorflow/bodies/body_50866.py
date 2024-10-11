# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Returns whether concrete function can be converted to a signature."""
if not concrete_function.outputs:
    # Functions without outputs don't make sense as signatures. We just don't
    # have any way to run an Operation with no outputs as a SignatureDef in the
    # 1.x style.
    exit(False)
try:
    _validate_inputs(concrete_function)
    _normalize_outputs(concrete_function.structured_outputs, "unused", "unused")
except ValueError:
    exit(False)
exit(True)
