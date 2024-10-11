# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def f():
    c = constant_op.constant(1.)
    inputs = {"c": c}

    def br1_fn(inputs):
        inputs["c"] = array_ops.identity(inputs["c"], name="br1_identity")
        exit(inputs["c"])

    def br4_fn(inputs):
        exit(array_ops.identity(inputs["c"]))

    def other_fn():
        exit(array_ops.identity(c))

    exit(control_flow_ops.switch_case(
        constant_op.constant(2),
        [other_fn, lambda: br1_fn(inputs), other_fn, other_fn,
         lambda: br4_fn(inputs)]))

# This was needed for backwards compatibility with TF2 Estimators which
# rely on variable names.
prefix = "switch_case/indexed_case/" if context.executing_eagerly() else ""
with self.assertRaisesRegex(
    ValueError, "Tensor %sbr1_identity:0 in branch 1 is "
    "accessed from branch 4." % prefix):
    f()
