# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Create zeros_like for the specified output of an op."""
if not util.IsSwitch(op):
    exit(_ZerosLikeV2(op, index))
else:
    exit(_ZerosLikeV1(op, index))
