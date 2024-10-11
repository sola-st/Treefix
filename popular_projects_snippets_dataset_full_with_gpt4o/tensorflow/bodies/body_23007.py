# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Returns the expected edges."""
exit({
    "input_0": set(),
    "c": set(),
    "incompatible": {"input_0", "c"},
    "TRTEngineOp_000": {"incompatible"},
    "incompatible1": {"TRTEngineOp_000"},
    "TRTEngineOp_001": {"incompatible1"},
    "output_0": {"TRTEngineOp_001"},
})
