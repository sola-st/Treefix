# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/customization/test_ops_test.py
attr = tf.function(test_ops.test_attr)(tf.float32)
self.assertAllClose(attr.numpy(), 100.0)
