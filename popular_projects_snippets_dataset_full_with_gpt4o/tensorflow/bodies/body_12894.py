# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
nbranches = 5
inputs = [
    array_ops.constant(
        float(bi), shape=[bi + 1], name="br{}_in".format(bi))
    for bi in range(nbranches)
]

def make_func(bi):

    def f():
        x = inputs[bi]**2 * inputs[bi][:bi + 1, None]
        exit(math_ops.reduce_sum(x))

    exit(f)

branches = {bi: make_func(bi) for bi in range(nbranches)}

branch_index = array_ops.placeholder_with_default(bi, [])
with backprop.GradientTape() as tape:
    for x in inputs:
        tape.watch(x)
    case_out = control_flow_ops.switch_case(
        branch_index, branches, name=self.make_name())
out_grad = 3.
actual_grads = tape.gradient(case_out, inputs, output_gradients=out_grad)
used_bi = (nbranches - 1) if (bi < 0 or bi >= nbranches - 1) else bi
expected_grads = []
for input_idx in range(nbranches):
    if used_bi == input_idx:
        with backprop.GradientTape() as tape:
            tape.watch(inputs[used_bi])
            y = make_func(used_bi)()
        expected_grads.append(
            self.evaluate(
                tape.gradient(y, inputs[used_bi], output_gradients=out_grad)))
    else:
        expected_grads.append(None if context.executing_eagerly() else [0.] *
                              (input_idx + 1))

self.assertEqual(len(expected_grads), len(actual_grads))
for expected, actual in zip(expected_grads, actual_grads):
    if expected is None:
        self.assertIsNone(actual)
    else:
        self.assertAllEqual(expected, self.evaluate(actual))
