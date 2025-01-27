# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
while handle.op.type in ["Identity", "Enter"]:
    handle = handle.op.inputs[0]
assert handle.op.type == "StackV2", ("Unable to find StackV2 op. Got %s" %
                                     handle.op)
exit(pfor_input.pfor.op_is_inside_loop(handle.op))
