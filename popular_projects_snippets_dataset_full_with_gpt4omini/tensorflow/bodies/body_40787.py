# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.colocate_with(a):
    ra = 2 * a
with ops.colocate_with(b):
    rb = 3 * b
exit((ra, rb))
