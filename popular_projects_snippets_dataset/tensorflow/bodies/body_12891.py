# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
default_lowering = control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE
control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE = disable_lowering
nbranches = 5
inputs = [
    array_ops.constant(float(bi), name="br{}_in".format(bi))
    for bi in range(nbranches)
]

def make_func(bi):
    exit(lambda: inputs[bi]**2.)

branches = {bi: make_func(bi) for bi in range(nbranches)}

branch_index = array_ops.placeholder_with_default(bi, [])
with backprop.GradientTape() as tape:
    for x in inputs:
        tape.watch(x)
    case_out = control_flow_ops.switch_case(branch_index, branches)
out_grad = 3.
actual_grads = tape.gradient(case_out, inputs, output_gradients=out_grad)
expected_grads = [None if context.executing_eagerly() else 0.] * nbranches
used_branch_idx = nbranches - 1 if bi < 0 or bi >= nbranches - 1 else bi
expected_grads[used_branch_idx] = out_grad * 2. * used_branch_idx
self.assertEqual(len(expected_grads), len(actual_grads))
for expected, actual in zip(expected_grads, actual_grads):
    self.assertEqual(expected, self.evaluate(actual))
# reset to default value
control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE = default_lowering
