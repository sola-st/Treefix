# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Note that we don't stack all the inputs. Hence unstacked values are printed
# once here vs multiple times in a while_loop.
pfor_input.stack_inputs([0])
outputs = _create_op(
    "Print", [x.t for x in pfor_input.inputs],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
exit([wrap(x, True) for x in outputs])
