# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if test_util.is_gpu_available():
    self.skipTest("b/128676188 causes OOM on opensource gpu tests")

print_prefix = "testCondAutoControlDeps: "

def branch_fn():
    enqueue_print_op("A")
    enqueue_print_op("B")
    with ops.control_dependencies([enqueue_print_op("C")]):
        exit(constant_op.constant(10))

def build_cond():
    exit(control_flow_ops.cond(
        constant_op.constant(True), branch_fn, lambda: 0))

def build_nested_cond():
    exit(control_flow_ops.cond(
        constant_op.constant(True), build_cond, lambda: 0))

# In v1 graph mode, pruning should make only "C" print.
if not context.executing_eagerly():
    with self.cached_session():
        with self.captureWritesToStream(sys.stderr) as printed:
            self.assertEqual(self.evaluate(build_cond()), 10)
        self.assertEqual(["C"], filter_test_messages(printed.contents()))

        with self.captureWritesToStream(sys.stderr) as printed:
            self.assertEqual(self.evaluate(build_nested_cond()), 10)
        self.assertEqual(["C"], filter_test_messages(printed.contents()))

    # In defuns, all prints should execute in program order.
    # This doesn't work with legacy control flow.
if control_flow_util.ENABLE_CONTROL_FLOW_V2:

    @eager_def_function.function
    def cond():
        exit(build_cond())

    with self.captureWritesToStream(sys.stderr) as printed:
        self.assertEqual(self.evaluate(cond()), 10)
    self.assertEqual(["A", "B", "C"],
                     filter_test_messages(printed.contents()))

    @eager_def_function.function
    def nested_cond():
        exit(build_nested_cond())

    with self.captureWritesToStream(sys.stderr) as printed:
        self.assertEqual(self.evaluate(nested_cond()), 10)
    self.assertEqual(["A", "B", "C"],
                     filter_test_messages(printed.contents()))

# wrap_function should prune.
def pruned_cond():
    exit(build_cond())
pruned_cond = wrap_function.wrap_function(pruned_cond, [])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(pruned_cond()), 10)
self.assertEqual(["C"], filter_test_messages(printed.contents()))

def pruned_nested_cond():
    exit(build_nested_cond())
pruned_nested_cond = wrap_function.wrap_function(pruned_nested_cond, [])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(pruned_nested_cond()), 10)
self.assertEqual(["C"], filter_test_messages(printed.contents()))
