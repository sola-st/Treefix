# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cpu = constant_op.constant([[1., 2.], [3., 4.]])
c2g = cpu.gpu()
self.assertAllEqual(c2g, cpu.numpy())
