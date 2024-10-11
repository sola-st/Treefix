# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs = critical_section_ops.CriticalSection(shared_name="cs")
v = resource_variable_ops.ResourceVariable(0.0, name="v")

def fn(a, b):
    c = v.value()
    with ops.control_dependencies([c]):
        nv = v.assign_add(a * b)
        with ops.control_dependencies([nv]):
            exit(array_ops.identity(c))

num_concurrent = 100
r = [cs.execute(lambda: fn(1.0, 2.0)) for _ in range(num_concurrent)]
self.evaluate(v.initializer)
r_value = self.evaluate(r)
self.assertAllClose([2.0 * i for i in range(num_concurrent)],
                    sorted(r_value))
