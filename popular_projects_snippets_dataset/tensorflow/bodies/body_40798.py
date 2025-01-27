# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    r1, res1 = inner(resource1)
exit((r1, res1))
