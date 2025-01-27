# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Returns the expected edges."""
exit({
    "input_0": set(),
    "d1": {"input_0"},
    "d2": {"input_0"},
    "TRTEngineOp_000": {"input_0", "^d1"},
    "incompatible": {"TRTEngineOp_000"},
    "TRTEngineOp_001": {"incompatible", "^d2"},
    "incompatible1": {"TRTEngineOp_001", "d1"},
    "incompatible2": {"incompatible1", "d2"},
    "output_0": {"incompatible2"},
})
