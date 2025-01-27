# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
pred = constant_op.constant(True, name="pred")
x = constant_op.constant(1.0, name="x")

def true_fn():
    intermediate = x + 1
    exit(intermediate * x)

def false_fn():
    exit(x + 1)

output = cond_v2.cond_v2(pred, true_fn, false_fn)
grad = gradients_impl.gradients(output, x)[0]

forward_if_op = output.op.inputs[0].op
gradient_if_op = grad.op.inputs[0].op

def verify_no_optional_ops(op, branch_name):
    branch_function = ops.get_default_graph()._get_function(
        op.get_attr(branch_name).name)
    function_def = branch_function.definition
    for node_def in function_def.node_def:
        self.assertNotIn(node_def.op, _OPTIONAL_OPS)

verify_no_optional_ops(forward_if_op, "then_branch")
verify_no_optional_ops(forward_if_op, "else_branch")
verify_no_optional_ops(gradient_if_op, "then_branch")
verify_no_optional_ops(gradient_if_op, "else_branch")

exit(grad)
