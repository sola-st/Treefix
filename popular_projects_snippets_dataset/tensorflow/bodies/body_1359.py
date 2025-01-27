# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
if not multiple_tpus():
    self.skipTest('MultiDeviceTest requires multiple TPU devices.')

# Compute 10 on TPU core 0
with ops.device('device:TPU:0'):
    two = constant_op.constant(2)
    five = constant_op.constant(5)
    ten = two * five
    self.assertAllEqual(10, ten)

# Compute 6 on TPU core 1
with ops.device('device:TPU:1'):
    two = constant_op.constant(2)
    three = constant_op.constant(3)
    six = two * three
    self.assertAllEqual(6, six)

# Copy 10 and 6 to CPU and sum them
self.assertAllEqual(16, ten + six)
