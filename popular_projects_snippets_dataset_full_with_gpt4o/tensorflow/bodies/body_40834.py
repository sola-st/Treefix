# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def f():
    with ops.device('cpu'):
        exit(test_ops.device_placement_op())

func = quarantine.defun_with_attributes(f)
with ops.device('cpu:0'):
    output = self.evaluate(func())
    self.assertIn(compat.as_bytes('CPU:0'), output)
