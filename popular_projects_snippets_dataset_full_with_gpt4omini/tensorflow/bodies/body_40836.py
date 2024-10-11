# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def multi_device_fn():
    with ops.device('/cpu:0'):
        s0 = test_ops.device_placement_op()
    with ops.device('/cpu:1'):
        s1 = test_ops.device_placement_op()
    with ops.device('/cpu:2'):
        s2 = test_ops.device_placement_op()
    s3 = test_ops.device_placement_op()
    exit((s0, s1, s2, s3))

defined = quarantine.defun_with_attributes(multi_device_fn)
outputs = self.evaluate(defined())
self.assertLen(total_function_cache(defined), 1)
self.assertIn(compat.as_bytes('CPU:0'), outputs[0])
self.assertIn(compat.as_bytes('CPU:1'), outputs[1])
self.assertIn(compat.as_bytes('CPU:2'), outputs[2])

with ops.device('/cpu:3'):
    outputs = self.evaluate(defined())
# All function definitions are agnostic to call site devices.
self.assertLen(total_function_cache(defined), 1)
self.assertIn(compat.as_bytes('CPU:0'), outputs[0])
self.assertIn(compat.as_bytes('CPU:1'), outputs[1])
self.assertIn(compat.as_bytes('CPU:2'), outputs[2])
self.assertIn(compat.as_bytes('CPU:3'), outputs[3])

with ops.device('/cpu:0'):
    outputs = self.evaluate(defined())
self.assertLen(total_function_cache(defined), 1)
self.assertIn(compat.as_bytes('CPU:0'), outputs[0])
self.assertIn(compat.as_bytes('CPU:1'), outputs[1])
self.assertIn(compat.as_bytes('CPU:2'), outputs[2])
self.assertIn(compat.as_bytes('CPU:0'), outputs[3])
