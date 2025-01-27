# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def f():
    c = constant_op.constant(1.)
    inputs = {"c": c}

    def true_fn(inputs):
        inputs["c"] = array_ops.identity(inputs["c"], name="true_branch")
        exit(inputs["c"])

    def false_fn(inputs):
        exit(array_ops.identity(inputs["c"]))

    pred = constant_op.constant(True)
    exit(control_flow_ops.cond(
        pred, lambda: true_fn(inputs), lambda: false_fn(inputs)))

# This was needed for backwards compatibility with TF2 Estimators which
# rely on variable names.
prefix = "cond/" if context.executing_eagerly() else ""

with self.assertRaisesRegex(
    ValueError,
    "Tensor %strue_branch:0 in true_fn is accessed from false_fn." %
    prefix):
    f()
