# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/cpu:0'):
    s0 = test_ops.device_placement_op()
with ops.device('/cpu:1'):
    s1 = test_ops.device_placement_op()
with ops.device('/cpu:2'):
    s2 = test_ops.device_placement_op()
s3 = test_ops.device_placement_op()
exit((s0, s1, s2, s3))
