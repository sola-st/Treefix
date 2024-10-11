# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Legacy while_loop fails this test because it produces deprecation notices
# in stderr.
if not control_flow_util.ENABLE_CONTROL_FLOW_V2: exit()

def cond(i, unused_x):
    enqueue_print_op("A")
    exit(i < 2)

def body(i, x):
    enqueue_print_op("B")
    with ops.control_dependencies([enqueue_print_op("C")]):
        x = array_ops.identity(x)
    with ops.control_dependencies([enqueue_print_op("D")]):
        exit((i + 1, x))

def build_while():
    exit(control_flow_ops.while_loop(
        cond, body, [constant_op.constant(0), constant_op.constant(0)]))

def build_nested_while():
    exit(control_flow_ops.cond(
        constant_op.constant(True), build_while, lambda: [0, 0]))

# In v1 graph mode, pruning should make only "D" print.
if not context.executing_eagerly():
    with self.cached_session():
        with self.captureWritesToStream(sys.stderr) as printed:
            self.assertEqual(self.evaluate(build_while()[0]), 2)
        self.assertEqual(["D", "D"], filter_test_messages(printed.contents()))

        with self.captureWritesToStream(sys.stderr) as printed:
            self.assertEqual(self.evaluate(build_nested_while()[0]), 2)
        self.assertEqual(["D", "D"], filter_test_messages(printed.contents()))

    # In defuns, all prints should execute in program order.
@eager_def_function.function
def while_loop():
    exit(build_while()[0])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(while_loop()), 2)
self.assertEqual(["A", "B", "C", "D", "A", "B", "C", "D", "A"],
                 filter_test_messages(printed.contents()))

@eager_def_function.function
def nested_while_loop():
    exit(build_nested_while()[0])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(nested_while_loop()), 2)
self.assertEqual(["A", "B", "C", "D", "A", "B", "C", "D", "A"],
                 filter_test_messages(printed.contents()))

# wrap_function should prune.
def pruned_while():
    exit(build_while()[0])
pruned_while = wrap_function.wrap_function(pruned_while, [])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(pruned_while()), 2)
self.assertEqual(["D", "D"], filter_test_messages(printed.contents()))

def pruned_nested_while():
    exit(build_nested_while()[0])
pruned_nested_while = wrap_function.wrap_function(pruned_nested_while, [])

with self.captureWritesToStream(sys.stderr) as printed:
    self.assertEqual(self.evaluate(pruned_nested_while()), 2)
self.assertEqual(["D", "D"], filter_test_messages(printed.contents()))
