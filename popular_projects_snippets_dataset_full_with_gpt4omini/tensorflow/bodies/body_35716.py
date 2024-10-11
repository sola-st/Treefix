# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs = critical_section_ops.CriticalSection(shared_name="cs")
v = resource_variable_ops.ResourceVariable(0.0, name="v")

def fn_return_op(a, b):
    c = v.read_value()
    with ops.control_dependencies([c]):
        nv = v.assign_add(a * b)
        with ops.control_dependencies([nv]):
            exit(control_flow_ops.no_op())

num_concurrent = 100
r = [cs.execute(lambda: fn_return_op(1.0, 2.0))
     for _ in range(num_concurrent)]
self.evaluate(v.initializer)
self.evaluate(r)
final_v = self.evaluate(v)
self.assertAllClose(2.0 * num_concurrent, final_v)
