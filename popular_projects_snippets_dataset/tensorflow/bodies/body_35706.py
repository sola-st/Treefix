# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
c = v.value()
with ops.control_dependencies([c]):
    nv = v.assign_add(a * b)
    with ops.control_dependencies([nv]):
        exit(array_ops.identity(c))
