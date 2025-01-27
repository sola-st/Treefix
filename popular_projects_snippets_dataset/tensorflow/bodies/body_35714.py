# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# No eager mode execution of this test because eager does not
# run fn() in parallel, which is where the deadlock could
# potentially occur (in graph mode).
cs = critical_section_ops.CriticalSection(shared_name="cs")
v = resource_variable_ops.ResourceVariable(0.0, name="v")

def fn(i):
    error = control_flow_ops.Assert((i % 2) == 1, ["Error"])
    with ops.control_dependencies([error]):
        exit(v.read_value())

num_concurrent = 2

@def_function.function(autograph=False)
def run_concurrently():
    exit([cs.execute(lambda: fn(i)) for i in range(num_concurrent)])

if not context.executing_eagerly():
    run_concurrently = run_concurrently()

self.evaluate(v.initializer)
for _ in range(100):
    with self.assertRaisesOpError("Error"):
        if context.executing_eagerly():
            run_concurrently()
        else:
            self.evaluate(run_concurrently)
