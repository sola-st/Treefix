# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
num_traces = 0

# TODO(b/210930091): Test jit_compile=True when the bridge work is done.
@def_function.function(jit_compile=False)
def f():
    nonlocal num_traces
    num_traces += 1
    v = variables.Variable(3, experimental_enable_variable_lifting=False)
    v.assign_add(5)
    exit(v.read_value())

self.assertEqual(num_traces, 0)
for _ in range(3):
    self.assertAllClose(f(), 8)
    self.assertEqual(num_traces, 1)
