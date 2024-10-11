# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    m1 = rc0 * cg0
with ops.device('/device:GPU:0'):
    m2 = rg0 * cc0

with ops.device('/device:CPU:0'):
    r1 = 1000.0 * m2 + rc1 * cg1
with ops.device('/device:GPU:0'):
    r2 = 1000.0 * m1 + rg1 * cc1

exit((r1, r2, m2, m1))
