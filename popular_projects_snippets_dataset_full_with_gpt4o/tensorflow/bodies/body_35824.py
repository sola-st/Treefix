# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
v1 = cls(1.0)
self.assertEqual(True, v1.trainable)

v2 = cls(1.0, synchronization=variables.VariableSynchronization.ON_READ)
self.assertEqual(False, v2.trainable)

v3 = cls(1.0, synchronization=variables.VariableSynchronization.ON_READ,
         trainable=True)
self.assertEqual(True, v3.trainable)

v4 = cls(1.0, synchronization=variables.VariableSynchronization.ON_READ,
         trainable=False)
self.assertEqual(False, v4.trainable)
