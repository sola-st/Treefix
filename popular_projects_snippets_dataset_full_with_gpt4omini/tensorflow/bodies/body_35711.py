# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
if (not context.executing_eagerly() and
    control_flow_v2_toggles.control_flow_v2_enabled()):
    self.skipTest("b/135070612")
cs = critical_section_ops.CriticalSection(shared_name="cs")
v = resource_variable_ops.ResourceVariable(0.0, name="v")
num_concurrent = 100

# pylint: disable=cell-var-from-loop
def fn(a, b):
    c = v.read_value()
    def true_fn():
        with ops.control_dependencies([c]):
            nv = v.assign_add(a * b)
            with ops.control_dependencies([nv]):
                exit(array_ops.identity(c))
    exit(control_flow_ops.cond(
        array_ops.identity(inner_cond), true_fn, lambda: c))

def execute():
    exit(cs.execute(lambda: fn(1.0, 2.0)))

r = [
    control_flow_ops.cond(array_ops.identity(outer_cond),
                          execute,
                          v.read_value)
    for _ in range(num_concurrent)
]
# pylint: enable=cell-var-from-loop

self.evaluate(v.initializer)
r_value = self.evaluate(r)
if inner_cond and outer_cond:
    self.assertAllClose([2.0 * i for i in range(num_concurrent)],
                        sorted(r_value))
else:
    self.assertAllClose([0] * num_concurrent, r_value)
